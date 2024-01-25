import tkinter as tk

class BaseScreen:
    """
    画面の基底クラスです。
    画面の基本的な機能を提供します。
    画面作成担当者はこのクラスを継承してください。
    from BaseScreen import BaseScreenでインポート
    class クラス名(BaseScreen):
    """
    def __init__(self, root: tk.Tk):
        """
        ウィンドウの基底クラスを初期化します。

        Parameters:
        - root: Tkinterウィンドウの親オブジェクト
        """
        self.root = root
        self.frame = tk.Frame(root)
        self.create_widgets()

    def create_widgets(self):
        """
        画面に表示されるウィジェットを生成・配置します。
        このメソッドはサブクラスでオーバーライドしてください。
        """
        pass

    def screen_show(self):
        """
        画面を表示します。
        """
        self.frame.pack(fill="both", expand=True)

    def screen_hide(self):
        """
        画面を非表示にします。
        """
        self.frame.pack_forget()