# 3人月の開発を2日間で ─ 日立グループ初の AI-DLC 実践で得たリアルな手応え | Amazon Web Services ブログ

# 3人月の開発を2日間で ─ 日立グループ初の AI-DLC 実践で得たリアルな手応え

by koheihy on 12 5月 2026 in [Developer Tools](https://aws.amazon.com/jp/blogs/news/category/developer-tools/ "View all posts in Developer Tools"), [General](https://aws.amazon.com/jp/blogs/news/category/general/ "View all posts in General"), [Kiro](https://aws.amazon.com/jp/blogs/news/category/artificial-intelligence/kiro/ "View all posts in Kiro") [Permalink](https://aws.amazon.com/jp/blogs/news/ai-dlc-unicorn-gym-hitachi-ics-202601/) Share

  * [](https://www.facebook.com/sharer/sharer.php?u=https://aws.amazon.com/jp/blogs/news/ai-dlc-unicorn-gym-hitachi-ics-202601/)
  * [](https://twitter.com/intent/tweet/?text=3%E4%BA%BA%E6%9C%88%E3%81%AE%E9%96%8B%E7%99%BA%E3%82%922%E6%97%A5%E9%96%93%E3%81%A7%20%E2%94%80%20%E6%97%A5%E7%AB%8B%E3%82%B0%E3%83%AB%E3%83%BC%E3%83%97%E5%88%9D%E3%81%AE%20AI-DLC%20%E5%AE%9F%E8%B7%B5%E3%81%A7%E5%BE%97%E3%81%9F%E3%83%AA%E3%82%A2%E3%83%AB%E3%81%AA%E6%89%8B%E5%BF%9C%E3%81%88&via=awscloud&url=https://aws.amazon.com/jp/blogs/news/ai-dlc-unicorn-gym-hitachi-ics-202601/)
  * [](https://www.linkedin.com/shareArticle?mini=true&title=3%E4%BA%BA%E6%9C%88%E3%81%AE%E9%96%8B%E7%99%BA%E3%82%922%E6%97%A5%E9%96%93%E3%81%A7%20%E2%94%80%20%E6%97%A5%E7%AB%8B%E3%82%B0%E3%83%AB%E3%83%BC%E3%83%97%E5%88%9D%E3%81%AE%20AI-DLC%20%E5%AE%9F%E8%B7%B5%E3%81%A7%E5%BE%97%E3%81%9F%E3%83%AA%E3%82%A2%E3%83%AB%E3%81%AA%E6%89%8B%E5%BF%9C%E3%81%88&source=Amazon%20Web%20Services&url=https://aws.amazon.com/jp/blogs/news/ai-dlc-unicorn-gym-hitachi-ics-202601/)
  * [](mailto:?subject=3%E4%BA%BA%E6%9C%88%E3%81%AE%E9%96%8B%E7%99%BA%E3%82%922%E6%97%A5%E9%96%93%E3%81%A7%20%E2%94%80%20%E6%97%A5%E7%AB%8B%E3%82%B0%E3%83%AB%E3%83%BC%E3%83%97%E5%88%9D%E3%81%AE%20AI-DLC%20%E5%AE%9F%E8%B7%B5%E3%81%A7%E5%BE%97%E3%81%9F%E3%83%AA%E3%82%A2%E3%83%AB%E3%81%AA%E6%89%8B%E5%BF%9C%E3%81%88&body=3%E4%BA%BA%E6%9C%88%E3%81%AE%E9%96%8B%E7%99%BA%E3%82%922%E6%97%A5%E9%96%93%E3%81%A7%20%E2%94%80%20%E6%97%A5%E7%AB%8B%E3%82%B0%E3%83%AB%E3%83%BC%E3%83%97%E5%88%9D%E3%81%AE%20AI-DLC%20%E5%AE%9F%E8%B7%B5%E3%81%A7%E5%BE%97%E3%81%9F%E3%83%AA%E3%82%A2%E3%83%AB%E3%81%AA%E6%89%8B%E5%BF%9C%E3%81%88%0A%0Ahttps://aws.amazon.com/jp/blogs/news/ai-dlc-unicorn-gym-hitachi-ics-202601/)
  * 


2026年1月22日〜23日、AWS Loft Tokyo にて11社87名が参加した「合同 AI-DLC Unicorn Gym」を開催しました。AI駆動開発ライフサイクル（AI-DLC）による開発プロセスの変革を体験いただくイベントです。イベント全体の詳細は「[11社合同 AI-DLC Unicorn Gym で体験した開発のパラダイムシフト](https://aws.amazon.com/jp/blogs/news/joint-ai-dlc-unicorn-gym-202601/)」をご覧ください。

本記事では、参加企業の一社である[株式会社日立産業制御ソリューションズ](https://www.hitachi-ics.co.jp/) 業務サポート本部デジタルイノベーションセンタ所属の竹地氏に、現場のエンジニアとしてAI-DLCを体験して感じた手応えを寄稿いただきました。

_以下、株式会社日立産業制御ソリューションズ 竹地氏による寄稿です。_

生成AIを開発に導入したものの、「思ったようにいかない」「自分で手を動かしたほうが早い」と悩む現場は多いのではないでしょうか。

株式会社日立産業制御ソリューションズの竹地です。当社は日立グループの一員として、製造業・社会インフラ向けのITソリューションや制御システムの開発を手がけています。私たちの開発チームも、まさに同様の課題を感じていました。

[![本記事について打ち合わせる早川（左）と竹地氏（右）](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/03/19/1000038536.jpeg)](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/03/19/1000038536.jpeg)

本記事について打ち合わせる早川（左）と竹地氏（右）

今回、2026年1月22日〜23日にAWS Loft Tokyoで開催された11社合同の「AI-DLC Unicorn Gym」に参加させていただきました。ここでは、要件定義（Inception）から設計・実装・デプロイ（Construction）に至る全工程をAI主導で進める開発プロセスを体験しました。従来なら3人月以上かかる規模の開発が、わずか2日間で形になるという成果を得ました。

本稿では、私たちが[AI-DLC（AI駆動開発ライフサイクル）](https://aws.amazon.com/jp/blogs/news/ai-driven-development-life-cycle/)の実践を通じて得た「リアルな手応え」と、これからのエンジニアに求められる「役割の変化」について共有します。

## 参加の背景

当社ではさまざまな生成AIを導入してきましたが、「期待通りに動かない」「信用できない」という声から、活用は局所的な補助に留まっていました。一方、AI技術の急速な進化を踏まえると、開発プロセスそのものを「AI前提」にアップデートする必要があります。

今回の Unicorn Gym では、AIコーディングエージェント「[Kiro](https://kiro.dev/)」を開発の主体に据えるAI-DLCを体験し、その実効性を検証することを目的としました。

## 実施内容

### テーマ：分散したIT資産・セキュリティデータの統合基盤構築

当社内にはIT資産、セキュリティ、プロジェクト収支など、形式も管理場所も異なるデータが複数のシステムに分散しており、必要な情報の抽出・結合に膨大な工数がかかっていました。社内で見積もったところ、この統合基盤を従来の手法で構築した場合は約530時間（3人月相当）の規模です。今回の Unicorn Gym では、この「IT資産・セキュリティデータの統合活用基盤」を2日間で構築できるか挑戦しました。

[![Unicorn Gym 当日の様子](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/03/19/DSC03587-1-scaled.jpg)](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/03/19/DSC03587-1.jpg)

Unicorn Gym 当日の様子

1日目の Inception（構想）では、Kiro との対話で曖昧なビジネス意図を詳細要件に変換しました。人間がレビュー・承認し、AIが仕様書に即時反映するサイクルを繰り返します。2日目の Construction（構築）では、前日の要件をもとに Kiro が設計・コードを提案し、モブコンストラクション形式で集中的に実装を進めました。

AI-DLCでは、エンジニアと業務部門の担当者（今回は資産管理の担当者や情報セキュリティの責任者）が肩を並べて作業し、AIの提案に対してその場でフィードバックを返します。「この項目は管理対象に含めるべきか」「このチェックロジックは現場の運用に合っているか」といった判断を、業務を熟知した担当者がその場で下せるため、数分後には修正された仕様書やコードが提示されます。この即時のフィードバックループが、AI-DLCの大きな強みです。

### 成果物と工数比較

開発工程 | AI-DLCでの成果物 | 手動開発の想定工数  
---|---|---  
要件定義・設計 | ユースケース・ストーリー8本、API設計14本 | 120〜160時間  
バックエンド | Lambda 18関数（約2,600行）、DynamoDB 9テーブル | 160〜200時間  
フロントエンド | ダッシュボードUI、RBAC（ロールベースアクセス制御）、CSV出力 | 120〜160時間  
インフラ・CI/CD | CDK 2系統、IAM設定、CI/CDパイプライン | 60〜80時間  
**合計** | **約70時間（7名×実働10時間）** | **約530時間（3人月相当）**  
  
![IT資産統合基盤のトップページ](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/03/19/a7125c9c-732d-4271-b3b2-72f9c6e2866d.png)

2日間で構築したIT資産統合基盤のメインページ

![IT資産統合基盤のダッシュボード画面](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/03/19/4f7c6f90-9386-444b-a2bb-6d410d3eb0d2.png)

2日間で構築したIT資産統合基盤のチェックページ

ただし、この成果には業務担当者が同席し即時に意思決定できる体制、業務割り込みのない集中環境、プロトタイプに特化したスコープ（結合テストやセキュリティ審査は未実施）という条件がありました。それでも、設計・実装からAWS環境へのデプロイまでを2日で形にできた点は、AI-DLCの可能性を強く実感する結果でした。

## 学び

### ① 設計の「ちょうどいい」を見極めるのは人間

Kiro はコード生成や設計提案において精度の高い回答を返してくれますが、時にプロジェクトの規模以上に厳格な構成を提案することがあります。今回も、小規模なバッチ処理に対して40ファイル以上のDDD（ドメイン駆動設計）構成が提示された場面がありました。「この規模であればシンプルな構成で十分」と判断し、方針を修正したのは人間です。AIが高品質な設計パターンを提案できるからこそ、それをプロジェクトの実情に合わせて取捨選択する判断力がより重要になります。

### ② コードの修正もAIに任せる

AIがミスをしたとき、自分でコードを直したくなります。しかし人間が直接手を加えると、AIが保持するコンテキストと実態に乖離が生じ、以降の提案精度が下がります。人間が修正した場合はその内容をAIに伝えることで乖離を防ぐこともできますが、基本的には修正もAIとの対話を通じて行い、「AIが認識しているコードが正」というルールを徹底することが、AI駆動開発をスムーズに回すための鍵でした。

### ③ 意思決定と言語化に集中する開発手法

AIは数分でレビュー結果を反映し、次の成果物を提出してきます。人間はコードを書く代わりに、レビューと意思決定を高速に繰り返します。また、AIは暗黙の前提や文脈を汲み取ることができないため、仕様や意図を正確に言語化する力が求められます。コーディングから解放された分、ビジネス価値の判断と要件の言語化に集中できる点が、AI-DLCの大きな魅力です。

## これからの展望

私たちが得た最大の収穫は、AI-DLCが単に時短のための開発手法ではないという点です。開発の密度とフィードバックの速度を高めることで、結果として開発全体が加速される ─ この体験は、従来の効率化とは質の異なるものでした。コードを書く作業はAIに委ね、人間はレビュー・承認に専念する。AIが一般的な設計パターンやベストプラクティスを瞬時に提示するからこそ、自社固有の業務制約や設計判断を見抜く技術力がより重要になります。

当社では今回の成果を踏まえ、AI-DLCのワーキンググループを発足する予定です。サンドボックス環境の整備やAIエージェントを使いこなすためのルール（Steering / Skills）の構築を進め、社内の開発プロセスへの適用を本格的に推進していきます。

_（寄稿ここまで）_   
AI-DLC に興味を持たれた方は、[aidlc-workflows（GitHub）](https://github.com/awslabs/aidlc-workflows)をご覧ください。Kiro を使ってAI-DLCを始めるためのワークフローやテンプレートを公開しています。   


![Unicorn Gym参加メンバー（日立産業制御ソリューションズ、AWS）](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/03/19/2026-03-11_13-52-01_621.jpg)

Unicorn Gym 参加メンバー（日立産業制御ソリューションズ、AWS）

### 著者

![竹地 航太郎](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/03/19/2026-03-11_13-44-14_914.jpg) | **竹地 航太郎**   
株式会社日立産業制御ソリューションズ 業務サポート本部デジタルイノベーションセンタ所属。クラウドや生成AIを活用したソフトウエア生産技術の社内展開を担当。AI‑DLC Unicorn Gymへの参加をきっかけに、AI駆動開発を取り入れた社内プロジェクトを推進中。  
---|---  
![早川 康平](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/03/19/2026-03-11_13-44-59_886.jpg) | **早川 康平**   
アマゾン ウェブ サービス ジャパン テクニカルカスタマーソリューションズ マネージャー。金融勘定系システムのPM、Webエンジニア、SaaSプロダクトマネージャー、ソリューションアーキテクトを経て現職。幅広い経験を活かし、日立グループ専任のCSMとして、SaaSアプリケーション開発やAI活用を含むクラウド活用と開発プロセスの変革を支援している。宮城県仙台市出身。  
  
TAGS: [CSM](https://aws.amazon.com/jp/blogs/news/tag/csm/)
