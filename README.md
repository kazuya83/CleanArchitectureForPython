# CleanArchitecture

## HexagonalArchitecture
[ヘキサゴナルアーキテクチャについてJavaで説明しているもの](https://github.com/thombergs/buckpal)をPythonで実装しなおしてみた
<img src="https://raw.githubusercontent.com/thombergs/buckpal/master/img/cover-packt-450.png" />

今回私が実装したディレクトリ構成
``` 
CleanArchitectureForPython/
  ├── HexagonalArchitecture/
  │   └── buckpal
  │       ├── Adpter
  │       │   ├── In
  │       │   │   └── Web
  │       │   └── Out
  │       │   │   └── Persistence
  │       ├── Application
  │       │   ├── Domain
  │       │   │   ├── Model
  │       │   │   └── Service
  │       │   └── Port
  │       │   │   ├── In
  │       │   │   └── Out
  │       └── Common
  └──  README.md
```
