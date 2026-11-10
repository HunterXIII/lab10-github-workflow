# Задание 4. Конфликт, merge и rebase

В [PR #11](https://github.com/HunterXIII/lab10-github-workflow/pull/11) вынес сообщения программы в [config.py](../config.py) и подключил его к CLI и сборке. От одной версии `main` создал две ветки. В [PR #12](https://github.com/HunterXIII/lab10-github-workflow/pull/12) изменил первую строку, а в [PR #13](https://github.com/HunterXIII/lab10-github-workflow/pull/13) — вторую. Открыл оба PR до слияния первого.

После слияния PR роли A GitHub показал конфликт у PR роли B. Изменения соседних строк попали в один участок патча. В обсуждениях оставил замечания от трёх ролей в рамках саморевью.

## Решение через merge

Выполнил `git merge origin/main` в ветке B. Получил:

```text
CONFLICT (content): Merge conflict in config.py
```

Сохранил обе строки, добавил файл через `git add config.py` и создал merge-коммит `5466ad2`. Исходные коммиты B сохранили SHA. Этот вариант отправил в PR и слил в `main`.

## Проверка через rebase

Создал [demo/4-rebase](https://github.com/HunterXIII/lab10-github-workflow/tree/demo/4-rebase) от исходного коммита B `3df238a` и выполнил `git rebase origin/main`. При переносе двух коммитов разрешил конфликт 2 раза через `git add config.py` и `git rebase --continue`. Итоговый коммит `fc2183d`. У перенесённых коммитов новые SHA, дополнительного merge-коммита нет.

В обоих вариантах содержимое файла совпало:

```python
VALID_EMAIL_MESSAGE = "Email подходит. Можно продолжить регистрацию."
INVALID_EMAIL_MESSAGE = "Некорректный email. Проверьте адрес и повторите ввод."
```

В обоих вариантах `python3 -B -m unittest -q` показал `Ran 6 tests` и `OK`. При слиянии выбрал merge, потому что ветка B уже опубликована. Для отката всего PR в `main` можно сделать `git revert -m 1 <SHA merge-коммита PR>` через новый PR. В линейной истории после rebase можно откатывать отдельные перенесённые коммиты, используя их новые SHA.
