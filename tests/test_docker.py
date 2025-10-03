"""
Test Docker containerization setup and functionality.
"""
import subprocess
import sys
import time
from collections.abc import Generator
from pathlib import Path

import pytest
import requests


class TestDockerSetup:
    """Test Docker configuration and setup."""

    def test_dockerfile_exists(self):
        """Test that Dockerfile exists."""
        dockerfile_path = Path("Dockerfile")
        assert dockerfile_path.exists(), "Dockerfile should exist"

    def test_dockerfile_has_required_content(self):
        """Test that Dockerfile contains required components."""
        dockerfile_path = Path("Dockerfile")
        if dockerfile_path.exists():
            content = dockerfile_path.read_text()

            required_elements = [
                "FROM python:",
                "WORKDIR /app",
                "COPY requirements.txt",
                "RUN pip install",
                "COPY src/",
                "EXPOSE 8501",
                "CMD",
                "streamlit",
            ]

            for element in required_elements:
                assert element in content, f"Dockerfile should contain '{element}'"

    def test_dockerfile_uses_secure_practices(self):
        """Test that Dockerfile follows security best practices."""
        dockerfile_path = Path("Dockerfile")
        if dockerfile_path.exists():
            content = dockerfile_path.read_text()

            # Should use non-root user
            assert "USER app" in content, "Dockerfile should use non-root user"

            # Should have healthcheck
            assert "HEALTHCHECK" in content, "Dockerfile should include health check"

            # Should use slim/alpine base image for smaller attack surface
            assert any(
                x in content.lower() for x in ["slim", "alpine"]
            ), "Dockerfile should use slim or alpine base image"

    def test_streamlit_app_exists(self):
        """Test that the main Streamlit application exists."""
        app_path = Path("src/streamlit_app.py")
        assert app_path.exists(), "Main Streamlit app should exist"

    def test_streamlit_app_is_valid_python(self):
        """Test that the Streamlit app is valid Python code."""
        app_path = Path("src/streamlit_app.py")
        if app_path.exists():
            # Try to compile the file
            with open(app_path) as f:
                code = f.read()

            try:
                compile(code, app_path, "exec")
            except SyntaxError as e:
                pytest.fail(f"Streamlit app has syntax error: {e}")


class TestDockerBuild:
    """Test Docker image building."""

    @pytest.mark.slow
    def test_docker_image_builds_successfully(self):
        """Test that Docker image can be built without errors."""
        try:
            result = subprocess.run(
                ["docker", "build", "-t", "csv-storyteller-test", "."],
                capture_output=True,
                text=True,
                timeout=300,  # 5 minute timeout
            )

            assert result.returncode == 0, f"Docker build failed: {result.stderr}"
            assert (
                "Successfully built" in result.stdout
                or "Successfully tagged" in result.stdout
            ), "Docker build should complete successfully"

        except subprocess.TimeoutExpired:
            pytest.fail("Docker build timed out after 5 minutes")
        except FileNotFoundError:
            pytest.skip("Docker not available in test environment")

    @pytest.mark.slow
    def test_docker_image_size_reasonable(self):
        """Test that the Docker image size is reasonable (< 2GB)."""
        try:
            # First build the image if not already built
            subprocess.run(
                ["docker", "build", "-t", "csv-storyteller-test", "."],
                capture_output=True,
                timeout=300,
            )

            # Check image size
            result = subprocess.run(
                ["docker", "images", "csv-storyteller-test", "--format", "{{.Size}}"],
                capture_output=True,
                text=True,
            )

            if result.returncode == 0:
                size_str = result.stdout.strip()
                # Parse size - could be in MB or GB
                if "GB" in size_str:
                    size_gb = float(size_str.replace("GB", "").strip())
                    assert (
                        size_gb < 2.0
                    ), f"Docker image too large: {size_str} (should be < 2GB)"
                elif "MB" in size_str:
                    # MB is fine, under 2GB
                    pass

        except (subprocess.TimeoutExpired, FileNotFoundError):
            pytest.skip("Docker not available or build failed")


class TestDockerRun:
    """Test Docker container execution."""

    @pytest.fixture
    def docker_container(self) -> Generator[str, None, None]:
        """Start a Docker container for testing and clean up after."""
        container_name = "csv-storyteller-test-run"

        try:
            # Stop and remove any existing container
            subprocess.run(["docker", "stop", container_name], capture_output=True)
            subprocess.run(["docker", "rm", container_name], capture_output=True)

            # Build the image first
            build_result = subprocess.run(
                ["docker", "build", "-t", "csv-storyteller-test", "."],
                capture_output=True,
                timeout=300,
            )

            if build_result.returncode != 0:
                pytest.skip("Docker build failed")

            # Start container in detached mode
            start_result = subprocess.run(
                [
                    "docker",
                    "run",
                    "-d",
                    "--name",
                    container_name,
                    "-p",
                    "8501:8501",
                    "csv-storyteller-test",
                ],
                capture_output=True,
                text=True,
            )

            if start_result.returncode != 0:
                pytest.skip(f"Failed to start container: {start_result.stderr}")

            # Wait for container to start
            time.sleep(10)

            yield container_name

        except (subprocess.TimeoutExpired, FileNotFoundError):
            pytest.skip("Docker not available")
        finally:
            # Cleanup
            subprocess.run(["docker", "stop", container_name], capture_output=True)
            subprocess.run(["docker", "rm", container_name], capture_output=True)

    @pytest.mark.slow
    def test_container_starts_successfully(self, docker_container):
        """Test that the Docker container starts and runs."""
        # Check if container is running
        result = subprocess.run(
            [
                "docker",
                "ps",
                "--filter",
                f"name={docker_container}",
                "--format",
                "{{.Status}}",
            ],
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0, "Failed to check container status"
        status = result.stdout.strip()
        assert "Up" in status, f"Container should be running, but status is: {status}"

    @pytest.mark.slow
    def test_streamlit_app_responds(self, docker_container):
        """Test that the Streamlit app responds to HTTP requests."""
        max_retries = 30
        for i in range(max_retries):
            try:
                response = requests.get("http://localhost:8501", timeout=5)
                if response.status_code == 200:
                    assert (
                        "CSV Storyteller Dashboard" in response.text
                    ), "Response should contain app title"
                    return
            except requests.RequestException:
                if i < max_retries - 1:
                    time.sleep(2)
                    continue
                else:
                    pytest.fail("Streamlit app did not respond after 60 seconds")

        pytest.fail("Streamlit app never became available")

    @pytest.mark.slow
    def test_container_health_check(self, docker_container):
        """Test that the container health check passes."""
        # Wait for health check to stabilize
        time.sleep(15)

        result = subprocess.run(
            [
                "docker",
                "inspect",
                docker_container,
                "--format",
                "{{.State.Health.Status}}",
            ],
            capture_output=True,
            text=True,
        )

        if result.returncode == 0:
            health_status = result.stdout.strip()
            # Health status should be "healthy" or at least not "unhealthy"
            assert (
                health_status != "unhealthy"
            ), f"Container health check failed: {health_status}"


class TestDockerCompose:
    """Test Docker Compose configuration if present."""

    def test_docker_compose_file_exists(self):
        """Test if docker-compose.yml exists (optional)."""
        compose_files = [
            Path("docker-compose.yml"),
            Path("docker-compose.yaml"),
            Path("compose.yml"),
            Path("compose.yaml"),
        ]

        # This is optional, so we just check if any exists
        existing_files = [f for f in compose_files if f.exists()]

        if existing_files:
            # If compose file exists, validate it has required structure
            import yaml

            compose_file = existing_files[0]
            with open(compose_file) as f:
                compose_data = yaml.safe_load(f)

            assert (
                "services" in compose_data
            ), "Docker Compose file should have services section"

            # Check if our app service is defined
            services = compose_data["services"]
            app_services = [
                name
                for name in services.keys()
                if "csv" in name.lower()
                or "storyteller" in name.lower()
                or "app" in name.lower()
            ]

            if app_services:
                app_service = services[app_services[0]]
                assert "ports" in app_service, "App service should expose ports"
                assert any(
                    "8501" in str(port) for port in app_service["ports"]
                ), "App service should expose Streamlit port 8501"
