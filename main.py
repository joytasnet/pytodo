import todo_dao as td

def main():
    todo_list=td.find_all()
    if not todo_list:
        print('Todoは1件もありません')
    else:
        for i,todo in enumerate(todo_list,1):
            print(f'{i} {todo}')
    print('--操作を入力してください--')
    if len(todo_list) == 0:
        select=int(input('1/登録 4/終了>>'))
    else:
        select=int(input('1/登録 2/重要度変更 3/削除 4/終了>>'))

    if select == 1:
        print('新規Todoを作成します。')
        title=input('Todo内容を入力してください>>')
        importance=int(input('重要度を1-10で入力してください>>'))
        td.insert_one(td.Todo(title,importance))
    if select == 2:
        idx=int(input(f'重要度を変更します。番号を入力してください(1~{len(todo_list)})>>'))-1
        todo=todo_list[idx]
        importance = int(input(f'[{todo.title}]の重要度を再設定してください>>'))
        todo.importance=importance
        td.update_one(todo)
        print('重要度を変更しました')

    if select == 3:
        idx=int(input(f'Todoを削除します。番号を入力してください(1~{len(todo_list)})>>'))-1
        if 0 <= idx < len(todo_list):
            title=todo_list[idx].title
            td.delete_one(todo_list[idx])
            print(f'[{title}]を削除しました')
        else:
            print('削除を中止しました')
    if select == 4:
        print('アプリケーションを終了します')
        return
    main()

main()
