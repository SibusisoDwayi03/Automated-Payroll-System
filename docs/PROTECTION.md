# Branch Protection Justification

Branch protection rules are enforced on the `main` branch to prevent accidental changes, enforce code review, and require that all tests pass before merging. This ensures that the `main` branch is always production-ready and stable.

## Rules Enforced:
- ✅ Require pull request reviews
- ✅ Require status checks to pass
- ✅ Prevent direct pushes to `main`
