# CleanArchitecture

## HexagonalArchitecture
[ヘキサゴナルアーキテクチャについてJavaで説明しているもの](https://github.com/thombergs/buckpal)をPythonで実装してみました。
<img src="https://raw.githubusercontent.com/thombergs/buckpal/master/img/cover-packt-450.png" />

基本、Javaに合わせて実装してみましたが、言語の特性上PythonではInterfaceが定義できなかったり、完全コンストラクタが実装できないので擬似的に実装してます。
あとは明示してませんが、言語差により異なる箇所がいくつかあります。

### 今回私が実装したディレクトリ構成
``` 
CleanArchitectureForPython/
  ├── HexagonalArchitecture/
      └── buckpal
          ├── Adpter
          │   ├── In
          │   │   └── Web
          │   └── Out
          │   │   └── Persistence
          ├── Application
          │   ├── Domain
          │   │   ├── Model
          │   │   └── Service
          │   └── Port
          │   │   ├── In
          │   │   └── Out
          └── Common
  
```
