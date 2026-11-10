# Задание 3. Релизный цикл и hotfix

1. Добавил [CHANGELOG](../CHANGELOG.md) через [PR #7](https://github.com/HunterXIII/lab10-github-workflow/pull/7) и выпустил [v1.0.0](https://github.com/HunterXIII/lab10-github-workflow/releases/tag/v1.0.0) с коммита `da15a60`.
2. В [PR #8](https://github.com/HunterXIII/lab10-github-workflow/pull/8) смоделировал регрессию после релиза. Упростил регулярное выражение так, что адрес `first.last@example.com` ошибочно отклонялся. Добавил [issue #9](https://github.com/HunterXIII/lab10-github-workflow/issues/9) с метками `bug` и `critical`.
3. Создал `hotfix/1.0.1` от тега `v1.0.0`. Подтянул `main` в hotfix отдельным merge-коммитом, чтобы исправить состояние, в котором ошибка уже появилась. Вернул поддержку точки и добавил регрессионный тест.
4. Слил [PR #10](https://github.com/HunterXIII/lab10-github-workflow/pull/10) в `main`. `Closes #9` закрыл bug issue автоматически. Обновил CHANGELOG и выпустил [v1.0.1](https://github.com/HunterXIII/lab10-github-workflow/releases/tag/v1.0.1) с коммита `560ae0a`.

## Как проверить

```bash
git log --first-parent --oneline hotfix/1.0.1
git tag --list 'v1.0.*'
python3 -B -m unittest -v
```

На версии с регрессией тест адреса с точкой падал. После hotfix локальный запуск показал `Ran 6 tests` и `OK`.

**Почему ветка hotfix начинается от тега?** Тег показывает, с какого выпущенного состояния начато срочное исправление. Подтягивание `main` позволяет применить правку к коду с уже внесённой регрессией.
