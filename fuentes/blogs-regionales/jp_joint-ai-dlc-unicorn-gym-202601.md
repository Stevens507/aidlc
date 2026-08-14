# 11 社合同 AI-DLC Unicorn Gym で体験した開発のパラダイムシフト | Amazon Web Services ブログ

# 11 社合同 AI-DLC Unicorn Gym で体験した開発のパラダイムシフト

by [稲田大陸](https://aws.amazon.com/jp/blogs/news/author/inariku/ "Posts by 稲田大陸") on 05 2月 2026 in [Amazon Q Developer](https://aws.amazon.com/jp/blogs/news/category/amazon-q/amazon-q-developer/ "View all posts in Amazon Q Developer"), [Best Practices](https://aws.amazon.com/jp/blogs/news/category/post-types/best-practices/ "View all posts in Best Practices"), [Developer Tools](https://aws.amazon.com/jp/blogs/news/category/developer-tools/ "View all posts in Developer Tools"), [Kiro](https://aws.amazon.com/jp/blogs/news/category/artificial-intelligence/kiro/ "View all posts in Kiro"), [Technical How-to](https://aws.amazon.com/jp/blogs/news/category/post-types/technical-how-to/ "View all posts in Technical How-to") [Permalink](https://aws.amazon.com/jp/blogs/news/joint-ai-dlc-unicorn-gym-202601/) Share

  * [](https://www.facebook.com/sharer/sharer.php?u=https://aws.amazon.com/jp/blogs/news/joint-ai-dlc-unicorn-gym-202601/)
  * [](https://twitter.com/intent/tweet/?text=11%20%E7%A4%BE%E5%90%88%E5%90%8C%20AI-DLC%20Unicorn%20Gym%20%E3%81%A7%E4%BD%93%E9%A8%93%E3%81%97%E3%81%9F%E9%96%8B%E7%99%BA%E3%81%AE%E3%83%91%E3%83%A9%E3%83%80%E3%82%A4%E3%83%A0%E3%82%B7%E3%83%95%E3%83%88&via=awscloud&url=https://aws.amazon.com/jp/blogs/news/joint-ai-dlc-unicorn-gym-202601/)
  * [](https://www.linkedin.com/shareArticle?mini=true&title=11%20%E7%A4%BE%E5%90%88%E5%90%8C%20AI-DLC%20Unicorn%20Gym%20%E3%81%A7%E4%BD%93%E9%A8%93%E3%81%97%E3%81%9F%E9%96%8B%E7%99%BA%E3%81%AE%E3%83%91%E3%83%A9%E3%83%80%E3%82%A4%E3%83%A0%E3%82%B7%E3%83%95%E3%83%88&source=Amazon%20Web%20Services&url=https://aws.amazon.com/jp/blogs/news/joint-ai-dlc-unicorn-gym-202601/)
  * [](mailto:?subject=11%20%E7%A4%BE%E5%90%88%E5%90%8C%20AI-DLC%20Unicorn%20Gym%20%E3%81%A7%E4%BD%93%E9%A8%93%E3%81%97%E3%81%9F%E9%96%8B%E7%99%BA%E3%81%AE%E3%83%91%E3%83%A9%E3%83%80%E3%82%A4%E3%83%A0%E3%82%B7%E3%83%95%E3%83%88&body=11%20%E7%A4%BE%E5%90%88%E5%90%8C%20AI-DLC%20Unicorn%20Gym%20%E3%81%A7%E4%BD%93%E9%A8%93%E3%81%97%E3%81%9F%E9%96%8B%E7%99%BA%E3%81%AE%E3%83%91%E3%83%A9%E3%83%80%E3%82%A4%E3%83%A0%E3%82%B7%E3%83%95%E3%83%88%0A%0Ahttps://aws.amazon.com/jp/blogs/news/joint-ai-dlc-unicorn-gym-202601/)
  * 


みなさん、こんにちは。ソリューションアーキテクトの稲田です。

2026 年 1 月 22 日〜23 日の 2 日間、AWS Loft Tokyo にて「合同 AI-DLC Unicorn Gym」を開催しました。日立産業制御ソリューションズ、三菱電機ビルソリューションズ、パナソニックエレクトリックワークス、DNP、TOPPAN、すかいらーく、JR東海、JTB、アルプスアルパイン、第一三共、しまうまプリント（順不同）の 11 社から計 87 名のエンジニア・ビジネスパーソンが集まり、AI による開発プロセスの変革を体験していただきました。

[![](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/02/02/DSC03672-1024x682.jpg)](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/02/02/DSC03672.jpg)

## AI 駆動開発ライフサイクル (AI-Driven Development Lifecycle, AI-DLC) とは

[AI 駆動開発ライフサイクル (AI-Driven Development Lifecycle, AI-DLC)](https://aws.amazon.com/jp/blogs/news/ai-driven-development-life-cycle/) は、AI を開発プロセスの中心に据えた新しい開発手法です。従来のソフトウェア開発手法は人間主導の長期的なプロセスとして設計されており、計画や会議などの本質的ではない活動に多くの時間が費やされてきました。AI をアシスタントとして単純に後付けするだけでは、その能力を制約し、時代遅れの非効率性を助長することにもなりかねません。

AI-DLC では「AI が実行し人間が監視する」というアプローチを取ります。AI が体系的に詳細な作業計画を作成し、積極的に意図のすり合わせとガイダンスを求め、重要な決定は人間に委ねます。ビジネス要件の文脈的理解と知識を持つのは人間だからです。そして、チームはリアルタイムでの問題解決、創造的思考、迅速な意思決定のために協力します。この孤立した作業から活気のあるチーム作業への転換が、イノベーションと成果物の提供を加速させます。

[![](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/02/02/aidlc-image03.png)](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/02/02/aidlc-image03.png)

## 2 日間で何が起きたか

各社はエンジニア 4〜6 名、ビジネスサイド 2 名の計 6〜8 名でチームを構成して参加しました。ビジネスとエンジニアが一体となって取り組むことが、AI-DLC の効果を最大化するポイントです。

1 日目は「Inception（開始）」フェーズ。午前中は AI-DLC の概要説明とチーム編成を行い、午後から本格的に Inception に取り組みました。各社が持ち寄ったテーマについて、AI がビジネス意図を詳細な要件、ストーリー、ユニットに変換していきます。これを「モブエラボレーション」と呼ばれる形式で進め、チーム全体が AI の質問や提案を積極的に検証しました。ビジネス担当者とエンジニアが同じ画面を見ながら議論することで、「何を作るのか」についての共通理解が深まっていきました。

＊エラボレーション（精緻化）: 学習中の新しい情報を既存の知識と関連付けていくことで、新たにインプットしている情報に詳細を付け加えていくプロセスのことです。エラボレーションのプロセスでは What (何を) 学習しているかよりも、学習中のトピックの背後にある How (どのように) や Why (なぜ) により重きを置きます。

[![](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/02/02/DSC03607-1-1024x682.jpg)](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/02/02/DSC03607-1.jpg)

第一三共チームの開発風景

2 日目は「Construction（構築）」フェーズ。朝から夕方まで集中的に実装に取り組みます。前日に固めた要件をもとに、AI が設計、コード、テストを提案します。「モブコンストラクション」を通じて、チームが技術的決定とアーキテクチャの選択についてリアルタイムで明確化していきました。17 時からは各社が成果を発表し、2 日間の学びを共有しました。発表会の後は懇親会。異なる業界のエンジニア同士が、AI 駆動開発の可能性について熱く語り合う姿が印象的でした。

[![](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/02/02/DSC03469-1024x682.jpg)](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/02/02/DSC03469.jpg)

三菱電機ビルソリューションズチームの開発風景

## 参加者が達成したこと

2 日間のワークショップで、数週間から数ヶ月を想定していた開発を完了させる成果が生まれました。

ある企業は IT 資産管理システムの開発に取り組み、フロントエンド、バックエンド、ダッシュボード構築を並行して進め、AWS 環境へのデプロイまで完了。当初 8 週間を想定していた開発が 2 日間で完了しました。

別の企業は、行動変容を促すサービスの PoC 用アプリケーションを開発。認証、アカウント登録、データ収集、通知機能を含む Web アプリを 2 日間で構築しました。

IoT センサデータを分析するクラウドシステムに取り組んだ企業は、UI とバックエンド API の連携まで 2 日間で完了。当初 6 ヶ月を想定していた内容でした。

金融機関向けシステムの更改に取り組んだ企業では、「要件定義のドキュメント化に 1 ヶ月近く、10 人弱で会議を重ねていた工程が、6 人で 2 日間に短縮された」という声がありました。

特筆すべきは、ある企業の部長職の方が 2 日間フルで参加し、自ら AI ツールをインストールしてプロダクト開発に取り組んだ事例です。マネジメント層が現場と同じ体験を共有することで、AI 駆動開発の価値を実感として理解できたと語っていました。

[![](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/02/02/DSC03422-1-1024x682.jpg)](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/02/02/DSC03422-1.jpg)

パナソニックエレクトリックワークスチームの開発風景

## 参加者の声

「システム開発に産業革命のような大きなインパクトを与えると感じた」

「パラダイムシフトを感じることができました」

「ビジネスサイドとの密なコミュニケーションで手戻りが大幅に減少した」

「会話を中心にプロジェクトを進めることが新鮮で、とても楽しく学びのある研修になりました」

イベント後のアンケートでは、満足度は 5 点満点中 4.56 点、98.8% の参加者が肯定的な評価を寄せました。そして 92.5% が継続的なフォローアップを希望しており、この 2 日間が「終わり」ではなく「始まり」として受け止められたことがわかります。

一方で、実務適用に向けた課題も見えてきました。最も多く挙がったのはセキュリティ・コンプライアンスに関する懸念です。社内のセキュリティ統制や、個人情報・機密情報の取り扱いをどうするか。また、既存の社内制度や承認プロセスとの整合をどう取るかという声もありました。AI が生成したコードのレビュー体制についても、「レビューする側の知識が追いつかない」という指摘がありました。これらは AI-DLC の導入が単なる技術導入ではなく、組織文化と制度の変革を伴うものであることを示しています。

[![](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/02/02/DSC03397-1024x682.jpg)](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/02/02/DSC03397.jpg)

しまうまプリントチームの開発風景

## これからの展開

AI-DLC は AI をうまく使うための方法ではありません。多くのお客様が語っている通り、AI-DLC は AI によって人と人のコミュニケーションをより活発に、円滑にします。これまでのソフトウェア開発において、最もボトルネックになっていたのは人間同士の認識合わせ、見解の調整とそのための準備（認識合わせのための詳細なドキュメンテーションや断続的な複数の会議、複数回のレビューによるゲートウェイなど）でした。これは、人間がアウトプットを担当する限り、書類などの準備にかかる時間があるために解決できない問題でした。AI はこれを変革します。AI のアウトプットの速さは関係者を一か所に集めた上でその場で意思決定のためのアウトプットを作成することを可能にします。これによって、ボトルネックが解消し、チームの意思決定の速度が劇的に向上します。

AI-DLC は特定のツールに依存した方法論ではないことも重要です。AI ツールの進化は早くそれはこれからより加速するでしょう。1 年後に皆さんがどのような AI ツールを利用しているかは誰にも予想できません。しかし、ツールだけでは真の課題は解決できないこともわかっています。AI による変革を実現するためにはみなさんの働き方そのものを変える必要があります。AI-DLC はウォーターフォールやアジャイルのようなソフトウェア開発の方法論を update し AI による変革を実現するためのガイドラインです。

今回の合同 AI-DLC Unicorn Gym をきっかけに多くの参加企業の方々がそれぞれの企業の文化やビジネスに合った形でのAIによる開発方法の変革を実現されると信じています。AWSはこれからもそれを支援し、また業界全体の発展のためにもそれぞれの発見や学びを共有できる機会を提供していきたいと考えています。

AI-DLC に興味を持たれた方は、ぜひ [aidlc-workflows](https://github.com/awslabs/aidlc-workflows) をチェックしてみてください。Kiro を使って AI-DLC を始めるためのワークフローやテンプレートが公開されています。

### 著者

![Photo of author](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2024/11/19/inariku-dev-live.png)

### [稲田 大陸 – いなりく](https://x.com/inada_riku)

AWS Japan で働く Kiro をこよなく愛すソリューションアーキテクト。普段は製造業のお客様を支援しています。その活動の傍ら、最近は [AI 駆動開発ライフサイクル (AI-DLC)](https://aws.amazon.com/jp/blogs/news/ai-driven-development-life-cycle/) の日本のお客様への布教活動もしつつ、[Kiro のブログ](https://aws.amazon.com/jp/blogs/news/introducing-kiro/)などを執筆しています。
