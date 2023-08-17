# XML 轉換成字典程式

這個 Python 程式將 XML 資料轉換成字典格式，以便進一步處理。它會從指定的 XML 檔案讀取輸入，並根據指定的利率計算在給定月份內的總金額。

## 前置需求

在執行程式之前，請確保您已經擁有以下內容：

- Python 3.x

## 開始使用

1. 將這個存儲庫複製到您的本地電腦，或者下載 `xml_to_dict_converter.py` 檔案。

2. 將名為 `setting.xml` 的 XML 檔案置於 `xml_to_dict_converter.py` 程式的相同目錄下。XML 檔案應該具有以下結構：

    ```xml
    <data>
        <money>10000</money>
        <interest>12</interest>
        <month>36</month>
    </data>
    ```

    根據需要調整 `<money>`、`<interest>` 和 `<month>` 的數值。

## 使用方式

1. 開啟終端機或命令提示字元。

2. 導航到包含 `xml_to_dict_converter.py` 程式和 `setting.xml` 檔案的目錄。

3. 使用以下命令執行程式：

    ```bash
    python xml_to_dict_converter.py
    ```

4. 程式將處理 XML 資料並計算總金額。結果將保存在名為 `result.txt` 的檔案中，並顯示在終端機中。

## 輸出結果

程式將生成一個名為 `result.txt` 的輸出檔案，內容如下：

# calculation-1

你最後剩下的錢為：<total_amount>

將 `<total_amount>` 替換為實際計算得出的總金額。

## 自訂化

您可以透過修改 `setting.xml` 檔案中的數值來自訂輸入資料。調整 `<money>`、`<interest>` 和 `<month>` 元素以符合您的需求。

## 作者

J.ROBERT.芭本海默

## 授權

本專案採用 [MIT 授權條款](LICENSE)。
