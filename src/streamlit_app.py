"""
Minimal Streamlit application for CSV Storyteller Dashboard.
This is a placeholder implementation to enable Docker testing.
"""
import streamlit as st


def main() -> None:
    """Main Streamlit application entry point."""
    st.set_page_config(
        page_title="CSV Storyteller Dashboard",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.title("📊 CSV Storyteller Dashboard")
    st.markdown(
        "### A local-first Python/Streamlit web app for CSV data exploration and AI-powered insights"
    )

    # Health check endpoint for Docker
    st.markdown("---")
    st.success("✅ Application is running successfully!")

    # Placeholder content
    st.info("🚧 This is a minimal implementation. Full features coming soon!")

    # Show configuration status
    st.markdown("### System Status")
    try:
        from src.config import config

        st.success(f"✅ Configuration loaded - LLM Provider: {config.llm_provider}")
        st.success(f"✅ Max file size: {config.max_file_size_mb}MB")
        st.success(
            f"✅ Offline mode: {'Enabled' if config.enable_offline_mode else 'Disabled'}"
        )
    except Exception as e:
        st.error(f"❌ Configuration error: {e}")


if __name__ == "__main__":
    main()
