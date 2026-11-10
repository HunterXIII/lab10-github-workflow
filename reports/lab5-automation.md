# Задание 5. SAST, секрет, staging и автоматизация issue

## SAST

[Workflow SAST](../.github/workflows/security.yml) проверяет `registration.py` и `config.py` сканером Bandit на PR в `main` и push в `main`. JSON-отчёт доступен в артефакте `bandit-report`. В [проверенном прогоне](https://github.com/HunterXIII/lab10-github-workflow/actions/runs/42778277684) отчёт содержал 0 находок. Изменения в [PR #14](https://github.com/HunterXIII/lab10-github-workflow/pull/14).

## Staging и секрет

Создал окружение `staging` с правилом доступа только для ветки `main`. Тестовое значение `API_TOKEN` хранится как секрет окружения. GitHub маскирует значение в логах, а workflow проверяет только наличие секрета.

[Workflow Staging](../.github/workflows/staging.yml) запускается вручную. В **Actions → Staging → Run workflow** нужно выбрать `main`. Job `test` сначала запускает тесты и собирает zipapp. От него через `needs` зависит `deploy-staging`. После успешной сборки приложение публикуется на [GitHub Pages](https://hunterxiii.github.io/lab10-github-workflow/). Изменения в [PR #15](https://github.com/HunterXIII/lab10-github-workflow/pull/15).

[Проверенный деплой](https://github.com/HunterXIII/lab10-github-workflow/actions/runs/42778370141) завершился успешно. Проверил журналы, значение `API_TOKEN` в них отсутствует. Скачанный со staging архив запустился:

```text
Введите email: Email подходит. Можно продолжить регистрацию.
```

## Команды issue

Создал метки `bug`, `feature`, `tech-debt` и milestone [Учебный спринт](https://github.com/HunterXIII/lab10-github-workflow/milestone/1). [Workflow команд](../.github/workflows/issue-commands.yml) обрабатывает комментарии владельца к issue. Срок хранится отдельной строкой в описании issue.

- `/assign @HunterXIII` назначает исполнителя.
- `/label feature` добавляет метку.
- `/due 2026-11-14` записывает срок.

В [учебной issue #17](https://github.com/HunterXIII/lab10-github-workflow/issues/17) проверил все три результата. Обработчик добавлен через [PR #16](https://github.com/HunterXIII/lab10-github-workflow/pull/16). Закрытие issue связано с PR отчётов через `Closes #17`.

**Почему секрет окружения?** Он доступен только job, использующему `staging` и прошедшему ограничение ветки.
