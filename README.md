# mouseselect-screenshot-windows
マウス選択範囲を連番で保存する簡易なスクリーンショットツールです(Window専用)<br>
<img src="https://user-images.githubusercontent.com/37477845/115104498-bf189400-9f93-11eb-9cdc-6e86db96a08c.gif" width="55%">

# Requirements
* PyAutoGUI 0.9.52 or Later
* OpenCV 3.4.2 or Later
* Pillow 6.1.0 or Later

# Usage
 
サンプルの実行方法は以下です。 <br>
起動後は以下の流れで操作します。<br>
1. CTRLキーを押下で選択開始(CTRLを押し続けている間選択)
2. 選択範囲をマウスカーソルで指定
3. CTRLキーを離すと選択された箇所のスクリーンショットを連番で保存
 
```bash
python main.py
```
* --file_ext<br>
スクリーンショットの拡張子<br>
デフォルト：jpg
* --output_path<br>
スクリーンショットの保存パス<br>
デフォルト：screenshot
* --unuse_debug_window<br>
デバッグ用の小窓の未使用化<br>
デフォルト：指定なし

# Author
高橋かずひと(https://twitter.com/KzhtTkhs)
 
# License 
mouseselect-screenshot-windows is under [Apache-2.0 License](LICENSE).

サンプル画像は[フリー素材ぱくたそ](https://www.pakutaso.com)様の写真を利用しています。
