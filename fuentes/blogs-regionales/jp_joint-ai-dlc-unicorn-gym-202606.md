# 9 社合同 AI-DLC Unicorn Gym：AI と作った 2 日間で見えた、 「書く」から「決める」への転換 | Amazon Web Services ブログ

# 9 社合同 AI-DLC Unicorn Gym：AI と作った 2 日間で見えた、 「書く」から「決める」への転換

by Minjung Oh on 22 7月 2026 in [Amazon Bedrock](https://aws.amazon.com/jp/blogs/news/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/ "View all posts in Amazon Bedrock"), [Developer Tools](https://aws.amazon.com/jp/blogs/news/category/developer-tools/ "View all posts in Developer Tools"), [Kiro](https://aws.amazon.com/jp/blogs/news/category/artificial-intelligence/kiro/ "View all posts in Kiro"), [Technical How-to](https://aws.amazon.com/jp/blogs/news/category/post-types/technical-how-to/ "View all posts in Technical How-to") [Permalink](https://aws.amazon.com/jp/blogs/news/joint-ai-dlc-unicorn-gym-202606/) Share

  * [](https://www.facebook.com/sharer/sharer.php?u=https://aws.amazon.com/jp/blogs/news/joint-ai-dlc-unicorn-gym-202606/)
  * [](https://twitter.com/intent/tweet/?text=9%20%E7%A4%BE%E5%90%88%E5%90%8C%20AI-DLC%20Unicorn%20Gym%EF%BC%9AAI%20%E3%81%A8%E4%BD%9C%E3%81%A3%E3%81%9F%202%20%E6%97%A5%E9%96%93%E3%81%A7%E8%A6%8B%E3%81%88%E3%81%9F%E3%80%81%20%E3%80%8C%E6%9B%B8%E3%81%8F%E3%80%8D%E3%81%8B%E3%82%89%E3%80%8C%E6%B1%BA%E3%82%81%E3%82%8B%E3%80%8D%E3%81%B8%E3%81%AE%E8%BB%A2%E6%8F%9B&via=awscloud&url=https://aws.amazon.com/jp/blogs/news/joint-ai-dlc-unicorn-gym-202606/)
  * [](https://www.linkedin.com/shareArticle?mini=true&title=9%20%E7%A4%BE%E5%90%88%E5%90%8C%20AI-DLC%20Unicorn%20Gym%EF%BC%9AAI%20%E3%81%A8%E4%BD%9C%E3%81%A3%E3%81%9F%202%20%E6%97%A5%E9%96%93%E3%81%A7%E8%A6%8B%E3%81%88%E3%81%9F%E3%80%81%20%E3%80%8C%E6%9B%B8%E3%81%8F%E3%80%8D%E3%81%8B%E3%82%89%E3%80%8C%E6%B1%BA%E3%82%81%E3%82%8B%E3%80%8D%E3%81%B8%E3%81%AE%E8%BB%A2%E6%8F%9B&source=Amazon%20Web%20Services&url=https://aws.amazon.com/jp/blogs/news/joint-ai-dlc-unicorn-gym-202606/)
  * [](mailto:?subject=9%20%E7%A4%BE%E5%90%88%E5%90%8C%20AI-DLC%20Unicorn%20Gym%EF%BC%9AAI%20%E3%81%A8%E4%BD%9C%E3%81%A3%E3%81%9F%202%20%E6%97%A5%E9%96%93%E3%81%A7%E8%A6%8B%E3%81%88%E3%81%9F%E3%80%81%20%E3%80%8C%E6%9B%B8%E3%81%8F%E3%80%8D%E3%81%8B%E3%82%89%E3%80%8C%E6%B1%BA%E3%82%81%E3%82%8B%E3%80%8D%E3%81%B8%E3%81%AE%E8%BB%A2%E6%8F%9B&body=9%20%E7%A4%BE%E5%90%88%E5%90%8C%20AI-DLC%20Unicorn%20Gym%EF%BC%9AAI%20%E3%81%A8%E4%BD%9C%E3%81%A3%E3%81%9F%202%20%E6%97%A5%E9%96%93%E3%81%A7%E8%A6%8B%E3%81%88%E3%81%9F%E3%80%81%20%E3%80%8C%E6%9B%B8%E3%81%8F%E3%80%8D%E3%81%8B%E3%82%89%E3%80%8C%E6%B1%BA%E3%82%81%E3%82%8B%E3%80%8D%E3%81%B8%E3%81%AE%E8%BB%A2%E6%8F%9B%0A%0Ahttps://aws.amazon.com/jp/blogs/news/joint-ai-dlc-unicorn-gym-202606/)
  * 


みなさん、こんにちは。ソリューションアーキテクトの呉(オ)です。

2026 年 6 月 11 日（木）〜 12 日（金）の 2 日間、AWS の拠点にて、9 社 11 チーム・約 90 名のお客様と一緒に AI-DLC Unicorn Gym（AI 駆動開発ライフサイクルを体験する実践型ワークショップ）を合同開催しました。参加各社が「自社の実際の業務課題」を持ち込み、Kiro と Claude Code を使って、ユーザーストーリーの作成からモック、実装、成果発表までを走り抜ける 2 日間です。

本記事では、複数社が同時に自社ワークロードで AI 駆動開発を体験したこの合同開催で何が起きたのか、どんな成果と気づきが生まれたのかをレポートします。

## AI 駆動開発ライフサイクル（AI-Driven Development Lifecycle, AI-DLC）とは

AI-DLC は、AI を開発プロセスの中心に据える開発手法です。AI をアシスタントとして後から付け足すのではなく、AI が実装を担い、人間は「何を作るか」「その出力は正しいか」を判断することに集中します。

プロセスは大きく 3 つのフェーズで構成されます。

  * Inception（インセプション）：解くべき課題を定義し、ユーザーストーリーへ分解する
  * Construction（コンストラクション）：AI と対話しながら並行して実装する
  * Operation（オペレーション）：運用・改善につなげる



特徴的なのは、「モブ」と呼ばれる進め方を重視する点です。モブとは、チーム全員が 1 つの画面を囲み、一人が操作役（ドライバー）となって手を動かしながら、残りのメンバー全員が意見を出し合い、その場で議論して進める共同作業のスタイルです。役割を固定して分業するのではなく、全員が同じ情報を見て一緒に考えることで、認識のズレを防ぎ、判断の質を高めます。AI-DLC では、要件を練り上げる Inception を全員で行う「モブエラボレーション」、実装を全員で進める Construction を「モブコンストラクション」と呼び、いずれもこのモブを基本形とします。Unicorn Gym ではこのプロセスを座学ではなく、自社の実テーマで 2 日間走り切ることで体で覚えていただきます。AI 駆動開発ライフサイクルの詳細については、[AI 駆動開発ライフサイクル：ソフトウェアエンジニアリングの再構築](https://aws.amazon.com/jp/blogs/news/ai-driven-development-life-cycle/) をご参照ください。

[![](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/21/aidlc-phases.png)](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/21/aidlc-phases.png)

## 9 社 11 チームが持ち込んだテーマ

今回集まったのは、事業ドメインの異なる 9 社でした。BtoB の卸・仕入れサイトや企業間決済・売掛保証サービスを展開するラクーン（ラクーンホールディングス）と、キャラクタービジネスで知られるサンリオは、それぞれ 2 チームで臨み、全体では 11 チームが同じ会場に机を並べました。DX 現場支援を強みとするメンバーズ、幅広い業界のシステム開発を担うテクノブレイブ・ニーズウェル・科学情報システムズ（SIS）、大手企業の DX 内製化を支援する情報戦略テクノロジー、法務業務を効率化するリーガルテックの GVA TECH、そしてコンビニ ATM 最大手のセブン銀行です。B2B プラットフォーム、エンターテインメント、システム開発、リーガルテック、金融と、まったく異なる事業領域のプレイヤーが一堂に会したことになります。

参加各社は、練習用の題材ではなく「今まさに解きたい実課題」を持ち込みました。テーマは、新規サービス機能の立ち上げ、社内基幹システムへの機能追加、営業支援、提案書ドラフトの自動生成、ピープルマネジメントなど多岐にわたります。

## Day 1: Inception 「まず何を作るか（作らないか）を決める」

初日の午前は、いきなり自社テーマに入るのではなく、まず AI-DLC の考え方の説明と共通題材を使ったハンズオンから始めました。Kiro の操作感やユーザーストーリーからモック作成、実装へと進める一連の流れを、全員が同じ題材で一度体験します。この助走を挟んでから本番に臨みました。チームは、各社が自社の PdM（プロダクトマネージャー）とエンジニアで編成しました。実際に手を動かして議論を主導するのはお客様自身で、AWS のメンバーは技術的に詰まったところの解消やフェーズの進め方のガイドに徹し、チームの自走を後押しする役に回りました。

午後からは、各チームが自分たちのテーマをユーザーストーリーへ分解する Inception に本格的に取り組みました。ここで多くのチームが口を揃えたのが、「まず対象を決めることに時間をかけたのが効いた」という気づきです。実装が速いからこそ、入口の「何を作るか」が成果を左右します。象徴的だったのは、「どこまで作るか」を大胆に絞り込んだチームです。セブン銀行のチームは、洗い出したユーザーストーリー 29 件のうち 13 件をその場でカットし、初日のうちに 16 件まで絞り込みました。サービスデザインの視点から参加したメンバーは、「どこまでを人間が決め、どこからを AI に委ねるか」という線引きこそが今回の一番の学びだったと振り返ります。スコープを決めるのは、あくまで人間の仕事だという実感です。その「人間が決める」を象徴する場面もありました。ラクーンのチームでは、AI がある機能を「マストだ」と提案してきました。しかし、同チームではその機能は当面手動運用でカバーできると割り切り、AI が「マスト」とした機能をあえて優先度の低い区分へ格下げしました。AI の提案をそのまま鵜呑みにするのではなく、事業の文脈を踏まえて人間が最終判断を下す、Inception ではこうした「AI が提案し、人間が決める」という役割分担が随所で見られました。また、AI にインタビューされながらユーザーストーリーを固めることで、リリース後の不正対策といった人間だけでは抜け落ちがちな観点まで AI が先回りして拾う場面も見られました。

[![](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/21/inception-sanrio-300x200.jpg)](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/21/inception-sanrio.jpg) [![](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/22/inception-needswell-1-300x200.jpg)](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/22/inception-needswell-1.jpg)

[![](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/21/inception-sis-1-300x200.jpg)](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/21/inception-sis-1.jpg) [![](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/21/showcase-seven-bank-300x200.jpg)](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/21/showcase-seven-bank.jpg)

_各チームの開発風景（サンリオ／ニーズウェル／科学情報システムズ／セブン銀行）_

## Day 2: Construction 「動くものを見ながら、その場で会話する」

2 日目は、並行して実装できるサブチームに分かれて実装を進め、最終成果発表へ向かいます。参加チームから最も多く声として挙がった一番の価値は、「動くものを見ながら、ビジネス側と開発側がリアルタイムに会話できたこと」でした。従来は、要望を伝えてから次のバージョンが上がってくるまで数週間のタイムラグがありました。それがこの 2 日間では目の前で動く成果物を見ながらその場で方向を変えられる、このフィードバックの即時性が多くのチームで共通の手応えになりました。一方で、AI が高速に生成物を出すぶん、「その出力が正しいかを判断し続ける」負荷が人間側に集中する、という声も複数上がりました。「もっともらしいコードがすぐ出るからこそ、正しさの見極めが難しい」「判断の連続で頭は疲れるが、面白い」「AI に任せるほど、人間の判断力が試される」 など、その手応えと難しさの両方を体感する時間でもありました。成果発表では、各チームが 2 日間で作り上げたものを発表しました。完成までたどり着いたチームや実装ゼロで並行開発の設計に振り切ったチーム、アプローチは様々でしたが、いずれも自社に持ち帰る具体的な手応えを掴んでいました。

[![](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/21/showcase-2-1.jpg)](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/21/showcase-2-1.jpg) [![](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/21/showcase-1-2.jpg) ](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/21/showcase-1-2.jpg)![](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/21/showcase-3-1.jpg)

[![](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/21/showcase-5-1.jpg)](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/21/showcase-5-1.jpg) [![](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/21/showcase-4-1.jpg) ](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/21/showcase-4-1.jpg)[![](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/21/showcase-6-1.jpg)](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/21/showcase-6-1.jpg)

[![](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/21/showcase-7-1.jpg)](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/21/showcase-7-1.jpg) [![](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/21/showcase-8-1.jpg)](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/21/showcase-8-1.jpg) ![](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/21/showcase-9-2.jpg)

[![](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/21/showcase-10-1.jpg)](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/21/showcase-10-1.jpg) [![](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/21/showcase-11-1.jpg)](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/21/showcase-11-1.jpg)[ ![](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/21/showcase-12-2.jpg)](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/21/showcase-12-2.jpg)

_各チームによる Day 2 成果発表の様子_

## 各チームのハイライトとお客様の声

成果発表で各チームが見せてくれた成果から、印象的だったものを紹介します。

新規アプリの運営管理画面に取り組んだチームは、「Kiro は 1ヶ月と見積もった。私たちは 2 日で 80% 終わった」と話します。Kiro が当初約 1 ヶ月と見積もった開発を 2 日間で 8 割完成させ、自社ドメインの実サブドメインへのデプロイまで到達しました。後回しにされがちな運営管理画面のような領域こそ、AI に任せることで一気に前へ進むという手応えが語られました。

既存の社内管理システムに操作履歴機能を追加したチームは、「2 ヶ月の開発が 2.5 日で見通せる可能性がある」と振り返ります。AI による既存ソースコードの読み込み精度の高さに驚き、従来 2 ヶ月相当の開発が 2.5 日で見通せる感触を得ていました。同時に「手戻り＝悪」という常識が覆り、「戻りやすさを設計しておけば、手戻りコストは構造的に低い」という発想の転換も語られました。

営業支援システムに取り組んだチームからは、「数人で数ヶ月分の差分が 1 日弱で出せた」という声が上がりました。実際に 1 日弱で約 14,000 行の差分を生成し、非エンジニアの責任者と事業ドメインの観点で議論できたことが最大の収穫だったと振り返ります。

5 人・5 台の PC で誰も 5 分以上手を止めない並行開発とコードを一切書かず AI とエンターキーだけで進めるという 2 つに取り組んだチームからは、「合意と設計に投資したら、コンフリクトはゼロになった」という言葉が生まれました。初日から 2 日目の午前まで一行もコードを書かず、全員が並行開発できる構造の設計に投資した結果、コンフリクトゼロで並行実装を走り切っています。クロージングの一言「Don’t write code, Write construct.（コードを書くな、構造を作れ）」は、AWS メンバーにも印象的でした。

商品企画出身の PdM が、「生まれて初めてプルリクエストを送れました」と語る場面も生まれました。AI との対話を通じて人生で初めて Pull Request (PR) を送り、さらに Inception のスキル化（AI がインタビューしてユーザーストーリーとドキュメントを生成し、PR でマージする仕組み）まで自作して再現性も確保していました。

これらの成果に加えて、合同開催ならではの声もありました。

「他社さんと一緒に取り組めたのがとても刺激的でした。発表で各社のドメインがにじみ出て、自社への適用イメージがどんどん湧きました。」「開発生産性がかなり上がることを実感しました。お客様への提供スピードが上がるので、ビジネスインパクトの面でも有意義でした。」「プロダクトを AI-DLC で作る経験ができて、純粋に楽しかったです。」

ポジティブな声だけではありません。

「判断の連続で疲れた」「AI に情報を渡し忘れ、AI が置いてけぼりになった」「既存システムの拡張は、作るべき範囲の議論が複雑になる」。こうした率直な気づきも、次に活かすための貴重な学びとして共有されました。

## 2 日間で見えた手応え

2 日間を通じて、参加各社が共通して手応えを感じたのは次の点でした。

  * 動くものを見ながら、ビジネスと開発がリアルタイムに会話できること
  * AI による既存コードの読み込み精度の高さ（レガシー資産の棚卸しに有効）
  * 音声入力がタイピングより圧倒的に速いこと
  * Inception をスキル化し、再現性と抜け漏れ防止を両立できること
  * 合意形成と設計に投資すれば、コンフリクトゼロの並行開発が実現できること



いずれも、「AI を開発の中心に据える」という進め方だからこそ生まれた実感です。

イベント後のアンケートでは、満足度は 5 点満点中 4.7 点、93.9% の参加者が肯定的な評価（4 点以上）を寄せています。また、体感された工数削減率は平均 74.0% にのぼりました。なお、継続して伴走支援を受けたいという声も多く寄せられ、この 2 日間が終わりではなくそれぞれの現場での始まりとして受け止められたことがうかがえます。

## おわりに

この 2 日間で最も印象的だったのは AI が実装を肩代わりするほど、人間の仕事が「書くこと」から「決めること」へと移っていく、という共通の実感でした。参加各社は、それぞれのドメインでその手触りを掴んで帰っていきました。そして、複数社が同じ場で真剣に取り組む合同開催だからこそ、互いの成果が刺激となり、自社でもできるという確信が生まれました。AWS はこうした AI 駆動開発への挑戦を、これからも各社の現場に寄り添いながら伴走していきます。

自社のワークロードで AI-DLC を試してみたい、という方は、ぜひお近くの AWS 担当者までお声がけください。AI-DLC に興味を持たれた方は、[aidlc-workflows](https://github.com/awslabs/aidlc-workflows) をチェックしてみてください。Kiro や Claude Code などを使って AI-DLC を始めるためのワークフローやテンプレートが公開されています。

[![](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/21/group-photo-1024x682.jpg)](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/21/group-photo.jpg)

_集合写真_

### 

### 著者

![Photo of author](https://d2908q01vomqb2.cloudfront.net/b3f0c7f6bb763af1be91d9e74eabfeb199dc1f1f/2026/07/21/DSC03049_square-300x300.jpeg)

### [Oh Minjung （オミンジョン）](https://x.com/kkam0907)

AWS Japan のソリューションアーキテクト。お客様のクラウドジャーニーにおける技術的なご支援をしています。その活動の傍ら、最近は [AI 駆動開発ライフサイクル(AI-DLC)](https://aws.amazon.com/jp/blogs/news/ai-driven-development-life-cycle/) の布教活動をしています。
