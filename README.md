# Hadenlabs - PHP Pre-commit Hooks

Pre-commit scripts appropiate for *any* PHP project. These hooks are made as 
custom plugins under the [pre-commit](http://pre-commit.com/#new-hooks) git hook framework.

# Setup

Just add to your `.pre-commit-config.yaml` file with the following

```yaml
- repo: git@github.com:hadenlabs/pre-commit-php.git
  sha: 
  hooks:
  - id: php-lint
```

# Supported Hooks

## php-lint

```yaml
- repo: git@github.com:hadenlabs/pre-commit-php.git
  sha: 
  hooks:
  - id: php-lint
```
