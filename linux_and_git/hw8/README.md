1. Создать новый репозиторий в github с названием git_intro
2. Создать папку и инициализируйте новый репозиторий у Вас на компьютере с таким же именем.
3. Скопировать любую картинку или фото в эту папку. 
4. Отправить эти изменения в репозиторий git_intro  в github. 

   Для этого после копирования фото сделайте: 

   ```console
   git init
   git add ИМЯ ФАЙЛА
   git commit -m "Added photo"
   git branch -M main
   git remote add origin git@github.com:ВАШЕ ИМЯ НА GITHUB/git_intro.git
   git push -u origin main
   ```
   
5. Прислать ссылку на Ваш репозиторий  git_intro с выполненными действиями.