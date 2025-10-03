# Development Workflow Instructions

## Overview
Systematic TDD workflow ensuring high code quality and consistent progress tracking.

## Development Workflow

### 1. Task Management
1. **Git Branch Setup**
   - Branch naming: `task/NNNN-description` (NNNN = zero-padded task number, e.g., `task/0042-user-authentication`)
   - Create from updated `dev` branch:
     ```bash
     git checkout dev && git pull upstream dev && git checkout -b task/NNNN-description
     ```

2. **Task Selection**
   - **If IN_PROGRESS.md has a task**: Continue working on it
   - **If no task in progress**:
      - Select top task from TODO.md
      - Analyze if achievable with this workflow
      - **If achievable**: Remove from TODO.md, add to IN_PROGRESS.md, create branch, continue
      - **If not**: halt with message "This task is too broad to achieve with this workflow. Please break it down into more atomic tasks or better define the requirements for optimal output."

3. **Task Types**
   - **Feature tasks**: Follow complete workflow below
   - **DevOps/infrastructure**: Abbreviated workflow focused on functionality validation

### 2. Test-First Development
1. Check for existing tests related to current feature
2. Write comprehensive tests validating all requirements (edge cases, errors, performance)
3. Lint and validate test code before committing
4. Commit with: `test: add tests for [feature]`

### 3. Feature Implementation
1. **Red-Green-Refactor**: failing tests → minimal implementation → refactor
2. **Guidelines**:
   - Follow project architecture/patterns
   - Strictly adhere to requirements (no scope creep)
   - Include documentation and type annotations
   - **DO NOT modify tests** to accommodate implementation
   - Always check `git status` before committing
   - **File Creation**: Use explicit operations to trigger filesystem events:
     ```bash
     touch path/to/file.py && echo "content" > path/to/file.py
     ```
   - Verify creation: `ls -la path/to/file.py`

### 4. Quality Assurance
1. Run full test suite to ensure all tests pass
2. Execute pre-commit hooks, fix any issues, re-run tests until all checks pass

### 5. Task Completion
1. **Update COMPLETED_TASKS.md** (MANDATORY before PR):
   - Append completed task with completion date and implementation details

2. **Clear IN_PROGRESS.md** (MANDATORY before PR):
   - Update to "No tasks are currently in progress."
   - Verify with `git diff IN_PROGRESS.md`

3. **Pre-PR Checklist**:
   - Verify COMPLETED_TASKS.md updated: `git diff COMPLETED_TASKS.md`
   - Verify IN_PROGRESS.md cleared: `git diff IN_PROGRESS.md`
   - Check `git status` for all relevant files

4. **Create Pull Request**:
   - Commit with format: `type(scope): concise description`
   - Use non-interactive flags (`--no-edit`, `--no-pager`)
   - Push: `git push origin task/NNNN-description`
   - Create PR against `dev` branch

5. **Update Local Dev**: After PR merge, `git checkout dev && git pull upstream dev`

6. Notify user of completion and readiness for next task

## File Operations & Git Guidelines

### Filesystem Operations
- **File Creation**: Use `run_in_terminal` with explicit operations:
  ```bash
  touch path/to/file.py && echo "content" > path/to/file.py
  ```
- **Verification**: Always verify with `ls -la` and `cat | head -5`
- Create incrementally, inform user of new files

### Git Commands
- **Avoid Interactive**: Use `--no-edit`, `--no-pager`, `--no-interactive`
- **Alternatives**: Use `git reset --soft` + new commit instead of interactive rebase

## Common Commands

```bash
# Branch management
git checkout dev && git pull upstream dev                    # Update dev
git checkout -b task/NNNN-desc && git push origin task/NNNN-desc # Create & push branch

# Testing & Quality
pytest tests/path/to/test_file.py -v                        # Run specific tests
pytest --cov=hootforge tests/                               # Run with coverage
pre-commit run --all-files                                  # Run all hooks
black . && ruff check . && mypy .                           # Linting tools

# Non-interactive Git
git commit --amend --no-edit                                # Amend without editor
git merge branch-name --no-edit                             # Merge without editor
git diff --no-pager && git log --no-pager -n 5             # Show without pagination
```
