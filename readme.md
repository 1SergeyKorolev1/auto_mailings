# Auto Mailings

сервис управления рассылками, администрирования и получения статистики

___
Пример: компания N захотела создать на нашем сервисе рассылку. Создала для нее сообщение, которое будет отправлено клиентам, наполнила базу клиентов своими данными с помощью графического интерфейса сайта, затем перешла к созданию рассылки: указала необходимые параметры, сообщение и выбрала клиентов, которым эта рассылка должна быть отправлена.
___

 /               | CRUD(create) | CRUD(read) | CRUD(update) | CRUD(delete) 
-----------------|--------------|------------|--------------|--------------
 Сущьности       | /            | /          | /            | /            
 Mailing        | +            | +          | +            | +            
 RecipientClient | +            | +          | +            | +            
 MailingMessage  | +            | +          | +            | +            
 Attempt         | auto         | -          | -            | +            