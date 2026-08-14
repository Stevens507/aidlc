# 【開催報告】ISV SaaS 事業者向け 8 社合同 AI-DLC Unicorn Gym | Amazon Web Services ブログ

# 【開催報告】ISV SaaS 事業者向け 8 社合同 AI-DLC Unicorn Gym

by Hiroki Yamazaki on 13 8月 2026 in [Amazon Bedrock](/jp/blogs/news/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/ "View all posts in Amazon Bedrock"), [Best Practices](/jp/blogs/news/category/post-types/best-practices/ "View all posts in Best Practices"), [Developer Tools](/jp/blogs/news/category/developer-tools/ "View all posts in Developer Tools"), [Kiro](/jp/blogs/news/category/artificial-intelligence/kiro/ "View all posts in Kiro"), [Technical How-to](/jp/blogs/news/category/post-types/technical-how-to/ "View all posts in Technical How-to") [Permalink](/jp/blogs/news/joint-ai-dlc-unicorn-gym-isv-202607/) Share

  * [](https://www.facebook.com/sharer/sharer.php?u=https://aws.amazon.com/jp/blogs/news/joint-ai-dlc-unicorn-gym-isv-202607/)
  * [](https://twitter.com/intent/tweet/?text=%E3%80%90%E9%96%8B%E5%82%AC%E5%A0%B1%E5%91%8A%E3%80%91ISV%20SaaS%20%E4%BA%8B%E6%A5%AD%E8%80%85%E5%90%91%E3%81%91%208%20%E7%A4%BE%E5%90%88%E5%90%8C%20AI-DLC%20Unicorn%20Gym&via=awscloud&url=https://aws.amazon.com/jp/blogs/news/joint-ai-dlc-unicorn-gym-isv-202607/)
  * [](https://www.linkedin.com/shareArticle?mini=true&title=%E3%80%90%E9%96%8B%E5%82%AC%E5%A0%B1%E5%91%8A%E3%80%91ISV%20SaaS%20%E4%BA%8B%E6%A5%AD%E8%80%85%E5%90%91%E3%81%91%208%20%E7%A4%BE%E5%90%88%E5%90%8C%20AI-DLC%20Unicorn%20Gym&source=Amazon%20Web%20Services&url=https://aws.amazon.com/jp/blogs/news/joint-ai-dlc-unicorn-gym-isv-202607/)
  * [](mailto:?subject=%E3%80%90%E9%96%8B%E5%82%AC%E5%A0%B1%E5%91%8A%E3%80%91ISV%20SaaS%20%E4%BA%8B%E6%A5%AD%E8%80%85%E5%90%91%E3%81%91%208%20%E7%A4%BE%E5%90%88%E5%90%8C%20AI-DLC%20Unicorn%20Gym&body=%E3%80%90%E9%96%8B%E5%82%AC%E5%A0%B1%E5%91%8A%E3%80%91ISV%20SaaS%20%E4%BA%8B%E6%A5%AD%E8%80%85%E5%90%91%E3%81%91%208%20%E7%A4%BE%E5%90%88%E5%90%8C%20AI-DLC%20Unicorn%20Gym%0A%0Ahttps://aws.amazon.com/jp/blogs/news/joint-ai-dlc-unicorn-gym-isv-202607/)
  * 


2026 年 7 月 16 日（木）、 17 日（金）の 2 日間、東京・麻布台ヒルズにて、ISV SaaS 事業者向けの 8 社合同 AI-DLC Unicorn Gym を開催しました。株式会社サイバーセキュリティクラウド、freee 株式会社、株式会社いえらぶ GROUP、モビルス株式会社、エムオーテックス株式会社、株式会社ヌーラボ、テクマトリックス株式会社、株式会社ヴァル研究所（順不同・敬称略）の 8 社から計 54 名にご参加いただき、各チームが自社プロダクトの開発テーマを持ち込んで、Kiro や Claude Code などの Coding Agent を活用しながら 2 日間 AI 駆動の開発プロセスを実践しました。

本記事では、ご参加いただいた各社が 2 日間 AI-DLC をどう体験したのか、参加者の声を交えてレポートします。

[![](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/08/03/IMG_0975_blurred-1024x768.jpg)](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/08/03/IMG_0975_blurred.jpg)

## AI-DLC (AI-Driven Development Lifecycle) とは

AI 駆動開発ライフサイクル（AI-DLC）は、AWS が提唱する、AI を開発プロセスの中心に据えた開発手法です。AI を単なるアシスタントとして使うのではなく、要件定義・設計・実装の主役を AI が担い、人間は「何を作るか」「その出力は正しいか」という意図のすり合わせと重要な判断に集中します。この役割分担により、従来は数ヶ月かかっていた要件定義から実装までの期間を数日に圧縮することを目指します。

AI-DLC の開発プロセスは Inception・Construction・Operations の 3 フェーズで構成されます。鍵となるのが、チーム全員で 1 つの画面を囲み、AI と対話しながら進める「モブワーク」というスタイルです。一人が操作役（ドライバー）となって手を動かし、残りのメンバー全員がその場で意見を出し合い、議論しながら進めます。Inception を全員で行うフェーズを「モブエラボレーション」、Construction をサブチームに分かれて進めるフェーズを「モブコンストラクション」と呼び、いずれもこのモブワークを基本形とします。AI が要件を整理し、選択肢やコードを素早く提示し、ビジネス・開発メンバーがその場で検証・判断する。この共同作業が、開発速度の向上だけでなく、ビジネスと開発のギャップを埋め、チーム全員の認識を揃える効果をもたらします。

[![](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/29/Screenshot-2026-07-29-at-13.56.10-1024x573.png)](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/29/Screenshot-2026-07-29-at-13.56.10.png)

AI-DLC の詳細については、[AI 駆動開発ライフサイクル：ソフトウェアエンジニアリングの再構築](/blogs/devops/ai-driven-development-life-cycle/) をご参照ください。

## AI-DLC Unicorn Gym 開催の背景と ISV SaaS 8 社が持ち込んだテーマ

AI-DLC Unicorn Gym は、AI-DLC を座学ではなく自社の実テーマで実践していただくプログラムです。各チームが実際の開発テーマを持ち込み、AI と対話しながらユーザーストーリーの作成から実装、成果発表までを 2 日間で走り切ることで、AI 駆動の開発プロセスによる効果を体感していただきます。

今回の AI-DLC Unicorn Gym は、ISV SaaS 事業者を対象とした複数社合同の形式で開催しました。AI-DLC Unicorn Gym 開催のご要望を多くいただいておりますが、複数日にわたって数十名の参加者を集めることがハードルとなり実施を断念されるケースもありました。複数社合同とすることで、各社 1 チームからの参加を可能にしました。

参加各社には、練習用の題材ではなく「自社の実際のプロダクト開発テーマ」をご用意いただきました。テーマは、既存プロダクトへの新機能追加、既存ページのリニューアル・モダナイズ、新規プロダクトの立ち上げ、業務プロセスの改善支援など多岐にわたりました。

[![](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/30/Screenshot-2026-07-30-at-15.38.51-1024x565.png)](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/30/Screenshot-2026-07-30-at-15.38.51.png)

## 2 日間のスケジュール

本イベントは、初日に Inception、2 日目に Construction を中心に据えた 2 日間の構成で実施しました。各日ともチーム全員が 1 つの画面を囲むモブ形式で進め、初日の終わりに中間報告会、2 日目の終わりに最終報告会を設けています。タイムスケジュールは目安であり、各チームの進捗状況に合わせて進めていただきました。

今回は AI-DLC の進行には Coding Agent 用のルールセットである [aidlc-workflows](https://github.com/awslabs/aidlc-workflows) をご利用いただきました。aidlc-workflows v2 が 7月に GA しましたので、詳しく知りたい方は [AI-DLC Workflows 2.0 のご紹介](https://speakerdeck.com/kanamasa/intro-of-ai-dlc-workflows2-dot-0) および [AI-DLC Workflow V1からV2へ：人間のボトルネックを解消する設計の進化](https://builder.aws.com/content/3HQgsojfwGT7m4UTYZHV2jMPcDU/ai-dlc-workflow-v1v2) をご確認ください。

_Day 1_

  * 9:30 キックオフ / AI-DLC Introduction
  * 10:00 aidlc-workflows EC サイト構築ハンズオン
  * 11:30 昼食
  * 12:30 Mob Elaboration（Inception）: 開発対象のスコープやユーザーストーリー、作業単位の精緻化
  * 17:15 中間報告会（1 日目の進捗状況を共有）



_Day 2_

  * 9:30 Mob Elaboration / Mob Construction :ドメインモデル設計、アーキテクチャコンポーネントの追加、プログラムやテストの作成
  * 11:30 昼食
  * 12:30 Mob Construction（各チームの進捗に応じて）
  * 17:00 最終報告会（成果・学びの共有）
  * 18:00 懇親会



[![](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/29/Screenshot-2026-07-29-at-13.52.07-1024x573.png)](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/29/Screenshot-2026-07-29-at-13.52.07.png)

## Day 1: Inception

初日の午後から、各チームが自分たちのテーマをユーザーストーリーへ分解する「モブエラボレーション」に取り組みました。チーム全員が 1 つの画面を囲み、AI と対話しながら要件を詳細化します。ビジネスメンバーも開発メンバーも同じ場で AI の提案を検証し、判断し、修正していきます。このプロセスを通じてチーム全員のコンテキストが揃い、その共通認識が Construction フェーズにそのまま引き継がれます。AWS からは、「5 分以上 AI を遊ばせない」、「HTML/CSS でモックを作りチームのイメージを合わせる」、「How に関する議論は Construction まで我慢する」などのガイドを提供しました。

複数のチームから、

> 「仕様を決める速さで AI-DLC の力を実感した」

> 「圧倒的に早いスピード感で一定動くものを作れたのは大きな発見」

といった、要件定義のスピード向上に関する感想をいただきました。

[![](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/08/03/IMG_9142_blurred-1024x677.jpg)](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/08/03/IMG_9142_blurred.jpg)

株式会社いえらぶ GROUP の開発風景

## Day 2: Construction

2 日目は、並行して実装できるサブチームに分かれて Construction を進め、最終報告会へ臨みます。AI が高速にコードを生成するなか、参加者はその方向性が適切かを検証・判断しました。

2 日間という短い時間ながら、8 チーム中 6 社がデモ可能な状態まで実装を完了しました。設計フェーズでの AI 活用に対して、

> 設計での AI という使い方で、よくできたフレームワーク。次回の新機能開発はこれで実施する。

といった手応えを語るチームもありました。

最終発表会では、「従来 1 ヶ月以上かかっていた要件定義フェーズが2日間で完了した」、「ジュニアメンバーが AI との対話を通じてドメイン知識へのキャッチアップを実現した」、といった成果の共有がおこなわれました。

[![](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/08/04/IMG_9131_blurred-1024x768.jpeg)](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/08/04/IMG_9131_blurred.jpeg)

## 参加者からのフィードバック

今回は参加者の方には AWS オフィスにお集まりいただき、各社様担当の営業メンバー・ソリューションアーキテクトがサポートをさせていただきました。モブワークという形式について、いくつものフィードバックをいただきました。

> 我々のチームのことをよく知るサポーターが、過度でもなく過小でもなく、適切なタイミングで声掛けしてもらえた

> 普段リモートワークなので、オフラインで一緒に開発できてよかった。フレームワークのおかげで会話が整理された。

また、ドキュメント作成やコーディングを高速にこなす AI に対して高頻度で意思決定・判断が求められることについて、

> 判断負荷が高いので、普段の業務時間だと後回しにしてしまいそう。集中して向き合えてよかった

という感想もいただきました。モデルの進歩により AI の自律性が高まる中、どこまでを人間が判断し、どこまでを AI に委ねるかはまさに今注目されている観点です。

イベント後のアンケートでは、80 % の参加者から最高点の ⭐︎5 評価をいただきました。「AI-DLC はあなたの働き方を変える可能性があるか」という問いに対しても平均 4.76 / 5.0 というご回答をいただきました。また平均工数削減率は 67.1%と、これまでの 3 倍の速度を実現できると体感していただきました。

## おわりに

AI がコードを書いてくれるようになると、人間の仕事は「書くこと」から「決めること」へと移っていきます。何を作るか (あるいは作らないか) を決めること、設計の方向性を判断すること、チーム間の認識を揃えること。AI-DLC がモブワークを重視するのは、この意思決定に集中できる環境を作るためです。

自社で AI-DLC を試してみたいという方は、まず [aidlc-workflows](https://github.com/awslabs/aidlc-workflows) をお試しください。Kiro や Claude Code などを使って AI-DLC を始めるためのワークフローやテンプレートが公開されています。AI-DLC は特定のツール・ワークフローに依存しない方法論です。皆様のこれまでの開発プロセスや組織構造、スキルセットなどによってカスタマイズして取り入れていただくことができます。

自社プロダクトを持つ ISV/SaaS 事業者にとって、AI-DLC はプロダクトの開発サイクルそのものを変えうる手法です。合同開催が「終わり」ではなく、それぞれの現場での「始まり」として受け止めていただき、この 2 日間の体験を各社の現場に持ち帰り、それぞれの形で活かしていただけることを楽しみにしています。

これまでの合同型 AI-DLC Unicorn Gym については以下のブログ記事もご覧ください。

  * [11 社合同 AI-DLC Unicorn Gym で体験した開発のパラダイムシフト](/jp/blogs/news/joint-ai-dlc-unicorn-gym-202601/)
  * [9 社合同 AI-DLC Unicorn Gym 大阪 ── AI と開発した 3 日間で見えた、人間の仕事](/jp/blogs/news/joint-ai-dlc-unicorn-gym-osaka-202605/)
  * [9 社合同 AI-DLC Unicorn Gym：AI と作った 2 日間で見えた、 「書く」から「決める」への転換](/jp/blogs/news/joint-ai-dlc-unicorn-gym-202606/)



### 筆者について

[![](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/31/E015GUGD2V6-U03960BJ84U-8a078cd1e37e-512-300x300.png)](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/31/E015GUGD2V6-U03960BJ84U-8a078cd1e37e-512.png)

#### [山崎 宏紀 (Hiroki Yamazaki)](https://x.com/yh1roki)

山崎宏紀 は Amazon Web Services Japan G.K. のソリューションアーキテクトとして、ISV/SaaS 業界のお客様を中心にアーキテクチャ設計や構築、生成 AI の活用・AI エージェントの開発をご支援しています。Kiro CLI や AWS CDK を好みます。(より良いご支援のために) AI エージェントに代わりに働いてもらおうと画策しています。
