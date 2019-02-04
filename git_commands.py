# to find files committed in git commit
# programmatic
git diff-tree --no-commit-id --name-only -r commit-id

# user-facing
git show --pretty="" --name-only commit-id