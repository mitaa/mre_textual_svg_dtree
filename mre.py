# -*- coding:utf-8 -*-

from textual.app import App
from textual.widgets import DirectoryTree

ROOT = r"foo"


class MyApp(App):
    # This works
    # def compose(self):
    #     yield DirectoryTree(ROOT)
    #     yield DirectoryTree(ROOT)

    # This doesn't
    def on_mount(self) -> None:
        self.mount(DirectoryTree(ROOT))
        self.mount(DirectoryTree(ROOT))

    def on_tree_node_highlighted(self, node):
        self.query(DirectoryTree)[-1].reload()


def main():
    app = MyApp()
    app.app.run()


if __name__ == "__main__":
    main()
