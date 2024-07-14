# tutorial-python-pytest

Pytest 是 Python 的專案測試框架，這可用於撰寫多樣的軟體測試，包括單元測試 ( unit tests )、整合測試 ( integration tests )、點對點測試 ( end-to-end tests )、功能性測試 ( functional tests )。

## 特徵說明

+ 設定檔按 configuration, https://docs.pytest.org/en/8.2.x/reference/customize.html
+ 前置處理 pytest plugin, https://docs.pytest.org/en/8.2.x/how-to/writing_plugins.html
+ 相依注入 ```@pytest.fixture```, https://docs.pytest.org/en/8.2.x/how-to/fixtures.html
+ 掛勾函數 ```@pytest.hookimpl```, https://docs.pytest.org/en/8.2.x/how-to/writing_hook_functions.html

## 目錄規劃

a. pytest 啟動句型可否為參數而非檔案
b. pytest 的 conftest 可否建立動態程式便於啟動執行
c. 使用 python 啟動 pytest 並建立必要的轉換程序

## BDD 框架

執行 ```pytest .\test\...\*.py``` 檔，此檔案會基於 pytest 規範需要引入對應 feature 目錄的 BDD 檔案。

但依據實務與案例經驗，BDD 進入點檔案具有高重複性，該檔案主要用於宣告應執行的 ```scenarios``` 與要引用的函式庫來源，並以此作為 pytest 目標；對此，設計一個基於 BDD 文檔來生成進入點檔案，並可執行 pytest 調用的 ```invoke_bdd.py``` 來執行 ```*.feature``` 的前置處理與執行，此外亦可基於團隊需要增加解析規則。

執行 ```python invoke_bdd.py arguments``` 來執行目標 ```arguments.feature``` 檔案 

## 驗證項目

#### 1、進入點 ```pytest``` 與 ```pytest.main``` 與測試檔搜尋與指定規則

參考文獻說明與範例 [invoke.py](src/invoke.py)，原則上 ```pytest.main``` 的函數可以使用字串設定出與 ```pytest``` 想同的執行命令，因此可以在執行前處理自身需要的程序。

#### 2、```pytest.ini``` 用途，規劃引用測試項與函式庫目錄

參考文獻說明，```pytest.ini``` 是將 ```pytest``` 的命令介面選項與參數以檔案方式匯入，可用於設定諸如進度顯示方式、記錄檔格式等。

#### 3、```conftest.py``` 用途，列舉 hook

參考文獻說明與範例 [conf](./conf) 中的 ```hooks_*.py``` 檔案，Hook 的用途是提供 pytest 工作流程中的鈎，讓開發者可以在測試執行前進行必要的資訊處裡與準備。

#### 4、設定 ```@pytest.hookimpl```

參考文獻說明，裝飾詞 ```pytest.hookimpl``` 是用來指定當前 Hook 函數的狀態，例如 trylast、tryfirst 這用來控制函數在此鈎內的執行順序。

#### 5、設定 ```@pytest.fixture```

參考文獻說明，裝飾詞 ```pytest.fixture``` 是相依注入設計，開發者指定一個函數使用此裝飾詞，並回傳一個物件，而此物件會依照執行的測試函數宣告引入回傳物件。

## 文獻

+ [Pytest.org](https://docs.pytest.org/)
    - [How to invoke pytest](https://docs.pytest.org/en/8.2.x/how-to/usage.html)
        + [pytest.main options](https://docs.pytest.org/en/8.2.x/reference/reference.html#pytest-main)
    - [Configuration](https://docs.pytest.org/en/8.2.x/reference/customize.html)
        + [pytest.ini options](https://docs.pytest.org/en/8.2.x/reference/reference.html#ini-options-ref)
    - [Writing hook functions](https://docs.pytest.org/en/8.2.x/how-to/writing_hook_functions.html)
        + [pytest bootstrapping hooks](https://docs.pytest.org/en/8.2.x/reference/reference.html#bootstrapping-hooks)
        + [Introduction To Pytest Hooks (A Practical Guide For Beginners)](https://pytest-with-eric.com/hooks/pytest-hooks/)
    - [How to use fixtures](https://docs.pytest.org/en/8.2.x/how-to/fixtures.html)
    - [Writing plugins](https://docs.pytest.org/en/8.2.x/how-to/writing_plugins.html)
    - [API Reference](https://docs.pytest.org/en/8.2.x/reference/reference.html)
+ 函式庫
    - [Allure Report](https://allurereport.org/docs/pytest/)
    - [Pytest BDD](https://pypi.org/project/pytest-bdd/)
+ 教學文件
    - [Python 測試入門 - PyTest Fixture](https://blog.tzing.tw/posts/python-testing-pytest-fixture-91b547f2)
