from .balance_editor import BalanceEditor

class MockUserRepository:
    def edit_balance(self,user_id, new_balance):
        pass

def test_edit():
    user_id = 1
    new_balance = 20.50

    balance_editor = BalanceEditor(MockUserRepository())

    response = balance_editor.edit(user_id, new_balance)

    assert response["type"] == "User"
    assert response["count"] == 1
    assert response["new_balance"] == new_balance
    