# Домашняя работа 22.1 Формы
_____
### Основное задание
* Для модели продуктов реализуйте механизм CRUD, задействовав модуль django.forms
 Условия для пользователей:
- могут создавать новые продукты,
- не могут создавать продукты с запрещенными словами в названии и описании.
Для исключения загрузки запрещенных продуктов реализуйте валидацию названия и описания продукта таким образом, 
чтобы нельзя было в них добавлять слова: 
казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар.
* Добавьте новую модель «Версия», которая должна содержать следующие поля:
- продукт,
- номер версии,
- название версии,
- признак текущей версии.

* Добавьте реализацию работы с формами для версий продукта.
_____

### * Дополнительное задание

В один момент может быть только одна активная версия продукта, поэтому при изменении 
версий необходимо проверять, что пользователь в качестве активной версии указал только одну. 
В случае возникновения ошибки вернуть сообщение пользователю и попросить выбрать только одну активную версию.
______

### Критерии выполнения заданий

* Результат выполнения проекта залейте на GitHub и сдайте в виде ссылки на репозиторий.

______