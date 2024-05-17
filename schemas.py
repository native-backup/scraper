from pydantic import BaseModel
from enum import Enum


class Unsei(str, Enum):
    unsei_1 = "胎"
    unsei_2 = "養"
    unsei_3 = "長生"
    unsei_4 = "沐浴"
    unsei_5 = "冠帯"
    unsei_6 = "建禄"
    unsei_7 = "帝旺"
    unsei_8 = "衰"
    unsei_9 = "病"
    unsei_10 = "死"
    unsei_11 = "墓"
    unsei_12 = "絶"


class Personalitytag(str, Enum):
    personality1 = "#飽き性"
    personality2 = "#甘えん坊"
    personality3 = "#誠実"
    personality4 = "#自由人"
    personality5 = "#やり抜く"
    personality6 = "#真面目"
    personality7 = "#神メンタル"
    personality8 = "#洞察力"
    personality9 = "#人見知り"
    personality10 = "#直感的"
    personality11 = "#探究心"
    personality12 = "#カリスマ"


class PersonalityDescription(str, Enum):
    personality1_description = "赤ちゃんが、与えたおもちゃに数ヶ月で飽きるように、飽き性、好奇心旺盛で、新規の取り組みに対する欲求が強い。"
    personality2_description = (
        "甘えん坊、人に頼ることが多く、自分で物事を解決することが苦手。"
    )
    personality3_description = "高い集中力、清潔感が有り、お洒落で穏やかな雰囲気を持つ。教養溢れる言動に加え、発言に対する信用力が高い"

    personality4_description = "海外に縁深く、学生時代に海外留学している方も多い。音楽、美術等、芸術、芸能センスがあり自由を愛し、束縛を嫌う"

    personality5_description = "プライド高めで粘り強く、やり抜く力が高い。強靭な精神を持つ大器晩成型。女性脳が強めで、女性管理に強みを持つ"

    personality6_description = "頑固で自他共に厳しく、愚痴ばかり口だけのみで努力しない人は許せない完璧主義者。強い責任感でコツコツ努力を積み重ねる"

    personality7_description = "型破りの活動派、学生起業し生涯トップで活躍する。多少の有事では、へこたれない強靭なメンタルを持つ生涯起業家"

    personality8_description = "一歩引いた視点で周りを見渡す事が得意。高い状況把握力を持つ。保守的でマイナス思考が強く、引っ込み思案な慎重派"

    personality9_description = "一人時間が好きな人見知りでシャイなのんびり屋。直観、創造力を備え、常にモクモク妄想、思考するアイデアの泉"

    personality10_description = "哲学、宗教、神社、占い等、スピリチュアル領域、精神世界を大事にし、第六感(直観)、正確な判断力を併せ持つ"

    personality11_description = "経済観念高く、誠心誠意、相手を大切にする地味で堅実な実業家。探究心が強く、何かしらテーマを探索し、深掘る"

    personality12_description = "継続、束縛が苦手な自由人。時間感覚も多少ルーズな一面を持ち、地上から数センチ浮いた雰囲気を持つ"


class PersonalityIndustryDescription(str, Enum):
    personality1_description = "独自アイデアを創発する優れた独創性を持つ。マイペースで、人と協調する事は苦手な為、一人で平和に働ける業界"
    personality2_description = "洞察力があり、人を育てるのが得意な為、教育関係や、愛されキャラを活用した人との触れ合いが多い業界"
    personality3_description = "人の真似が得意で、教わったことはすぐ再現する力、持ち前のデータ、数字を扱う能力、素早い判断力が活かせる業界"
    personality4_description = "海外に縁があり、華やかな芸能、アート等、趣味を実益にし、熱し易く冷め易い為、持続して興味、好奇心を持てる業界"
    personality5_description = "流行への敏感さ、独自の美的センス、発想、社交性が活かせる華やかで前向きな挑戦を許容できる前進的な業界"
    personality6_description = "仕事ができる人が好きな為、高い完成度が要求され、ストレス環境が高く、市場の競争環境が激しく上昇志向が強い業界"
    personality7_description = "負けず嫌い、命令、指図が大嫌いで雇われは不向きな為、下積み期間を飛ばし、近い将来に独立、起業がし易い業界"
    personality8_description = "人生経験が豊富で、知恵、経験則、洞察力を活かし、冷静に物事を対処することが要求される縁の下の力持ち的な業界"
    personality9_description = "人並外れた想像力、美的センスを持ち、次々とアイデアが溢れ出る為、感受性豊かなクリエイターの地位が高い業界"
    personality10_description = "ストイック、安定志向、使命感が強い為、徹底的な事前リサーチを要求され、安定性、強い使命感が感じられる業界"
    personality11_description = "「観察力」「情報収集、分析力」「質問力」が持ち味となる為、分析関連の仕事が多く発生する業界"
    personality12_description = "持ち味の「直感力」を活かし、「臨機応変さ」、「アドリブ力」を要求される変化が激しく楽しめる業界"


class IndustryTag(str, Enum):
    industry1 = "#コンサル"
    industry2 = "#デザイン"
    industry3 = "#教育"
    industry4 = "#ペット"
    industry5 = "#IT"
    industry6 = "#メディア"
    industry7 = "#芸能"
    industry8 = "#商社"
    industry9 = "#コスメ"
    industry10 = "#ファッション"
    industry11 = "#スタートアップ"
    industry12 = "#不動産"
    industry13 = "#伝統工芸"
    industry14 = "#音楽"
    industry15 = "#アート"
    industry16 = "#医療"
    industry17 = "#金融"
    industry18 = "#旅行"


class IndustryFieldTag(str, Enum):
    industry_field1 = "#コンサル"
    industry_field2 = "#新規事業家"
    industry_field3 = "#VC"
    industry_field4 = "#人事"
    industry_field5 = "#教師"
    industry_field6 = "#新規開拓営業"
    industry_field7 = "#商品企画"
    industry_field8 = "#海外マーケティング"
    industry_field9 = "#デザイナー"
    industry_field10 = "#アーティスト"
    industry_field11 = "#商品企画(女性向け)"
    industry_field12 = "#マーケティングリーダー"
    industry_field13 = "#商社営業"
    industry_field14 = "#起業家"
    industry_field15 = "#ベンチャーキャピタリスト"
    industry_field16 = "#UXリサーチャー"
    industry_field17 = "#クリエイター"
    industry_field18 = "#企画家"
    industry_field19 = "#R&D研究者"
    industry_field20 = "#リサーチャー"
    industry_field21 = "#芸能人"


class IndustryFieldDescription(str, Enum):
    industry_field_description_1 = "新規制のある事に対する好奇心が強く飽き性気質な為、数ヶ月単位で変化が激しく起こる飽きないオシゴト"
    industry_field_description_2 = "新規制のある事に対する好奇心が強く飽き性気質な為、数ヶ月単位で変化が激しく起こる飽きないオシゴト"
    industry_field_description_3 = "常識的、素直で、清潔感があり、話す内容が信用され易い為、営業、交渉事等で短期間で結果が出やすいシゴト"
    industry_field_description_4 = "語学力を活かせ、海外転勤可能性があり、強い感性、創造性を生かせスケールの大きな挑戦ができるオシゴト"
    industry_field_description_5 = "女性脳が強めで女性理解、管理は得意。トレンドを掴む直観力を活かし、リーダーシップを発揮できるオシゴト"
    industry_field_description_6 = "仕事大好き人間で、競争、努力が得意。男性脳が強めな為、リーダーシップを発揮し、男性チームを率いるオシゴト"
    industry_field_description_7 = "年功序列は関係なく、結果至上主義の強い組織でチームリーダー、トップを担える可能性があるオシゴト"
    industry_field_description_8 = "深い洞察力で本質、インサイトを見抜くことが得意。豊富な知識と積み重ねた経験を武器にしたオシゴト"
    industry_field_description_9 = "妄想癖が強く、頭の中では常にアイデアに満ち溢れる。斬新なアイデアを常に要求されるオシゴト"
    industry_field_description_10 = "直観力が鋭く嘘を見抜くことが得意で人を見る目がある。正確な判断力とリサーチ、分析力が活かせるオシゴト"
    industry_field_description_11 = "完璧な資料作成、得意な情報収集力、人間観察力を活かし、探究心を持てるテーマが見つけられるオシゴト"
    industry_field_description_12 = "芸能界のように時間的縛りが無く、組織の枠組みにはまらず、独自の視点、感性が活きる非定型なオシゴト"


class CultureTag(str, Enum):
    culture1 = "#平和主義"
    culture2 = "#愛情主義"
    culture3 = "#誠実主義"
    culture4 = "#自由主義"
    culture5 = "#平等主義"
    culture6 = "#努力家集団"
    culture7 = "#実力主義"
    culture8 = "#職人気質"
    culture9 = "#心理的安全性"
    culture10 = "#ミッション性"
    culture11 = "#オタク気質"
    culture12 = "#変化主義"


class CultureTagDescription(str, Enum):
    culture1_description = (
        "穏やかな性格な為、過剰な激務でなく、人当たりが強い人が多く存在しない平和な組織"
    )
    culture2_description = "安心感、愛情を感じ取れ、周囲に頼れる先輩が存在する面倒見の良いアットホームな組織"
    culture3_description = "自分にも相手にも嘘をつけない率直な性格な為、情報透明性が高く、誠実で真っ直ぐな組織"
    culture4_description = "古いルール、慣習にこだわり、束縛を強いる事がなく、枠に囚われない自由闊達な風土の組織"
    culture5_description = "高いプライドを逆撫でせず、入社直後から、年次関係なく、責任あるリーダー職を任せる組織"
    culture6_description = "プロとして努力を積み重ね結果を出す意識が高く、ストイックでモチベーションが高い組織"
    culture7_description = (
        "年齢、性別、人種関係なく、結果を出した人が正当評価され、昇進昇格していく組織"
    )
    culture8_description = (
        "特定分野に対する深い見識、技術を保有するスペシャリストが評価される組織"
    )
    culture9_description = "繊細で人目を気にし過ぎストレスを溜め易い為、心理的安全性高く、伸び伸びと安心できる組織"
    culture10_description = "死生観を持ち、ストイックにパーパス達成に向けて一丸となって邁進するミッションドリブンな組織"
    culture11_description = "情報収集力、マニアックな知識が持ち味の為、特定領域への偏愛性、知見が評価される組織"
    culture12_description = "変化中毒の為、定期的に案件、チームが変わり、常に変化を楽しめ、働き方に自由度の高い組織"


class TeamMemberTag(str, Enum):
    team_member1 = "#現実主義"
    team_member2 = "#面倒見が良い"
    team_member3 = "#長期視点"
    team_member4 = "#海外思考"
    team_member5 = "#フラット"
    team_member6 = "#努力家"
    team_member7 = "#フォロワー"
    team_member8 = "#背中を押す"
    team_member9 = "#具現者"
    team_member10 = "#誠実"
    team_member11 = "#優しい"
    team_member12 = "#放任"


class AdvideTag(str, Enum):
    advide1 = "#刺激度チェック"
    advide2 = "#落ち着き"
    advide3 = "#自然体"
    advide4 = "#ミッション共感"
    advide5 = "#フラットな組織"
    advide6 = "#傾聴する"
    advide7 = "#裁量権チェック"
    advide8 = "#箱から飛び出す"
    advide9 = "#自己開示する"
    advide10 = "#最後は直観"
    advide11 = "#早めに頼る"
    advide12 = "#自由度チェック"


class AdvideDescription(str, Enum):
    advide1_description = "根からの飽き性で好奇心旺盛な為、新卒が必ずしも天職でなく、2-3回転職し、本当に自分に合う刺激的な仕事に出逢うのが大事"
    advide2_description = "頼りたい、甘えたい欲望が奥底にあり、歳上からの引き上げられる。持ち前の可愛がられ力を活かせる職場は確認が大事"
    advide3_description = "純粋で心が清らか且つ本当の気持ちを素直に表現できるタイプで、嘘やごまかしを嫌う為、その会社で自然体の自分でいられるかが大事"
    advide4_description = "長続きしない飽き症の性格から自分を見失い転職を繰り返す為、人生の目的に沿った企業か上位概念への共感度合いの確認が大事"
    advide5_description = "負けず嫌いでプライドが高く、自分の意見をはっきりと主張し、信念を曲げない為、フラットな風通しの良い組織風土か確認が大事"
    advide6_description = "完璧主義、まじめ過ぎで、自分の意見、主張をハッキリと言い、譲らない為、適度な息抜きを挟み、相手の意見に耳を傾けることも大事"
    advide7_description = "圧倒的な自立心を持ち、本来、起業が最適。上位下達文化は苦手な為、フラットな組織で早期にリーダーシップを発揮できるか確認することが大事"
    advide8_description = "一歩下がり、全体像を洞察することは得意。ただ、転職は自分が主人公。人は他人に興味はない。行動力発揮し自分の箱から飛び出すことが大事"
    advide9_description = "ナルシストで初対面の人全員に心を開かない為、本当に理想的な転職を実現すべく、意識的に自己開示し真の理解者、アドバイザーを得ると良い"
    advide10_description = "正確な判断力がある為、応募案件、オファー案件等、意思決定で、何か迷いが出たら、優れた直観力をベースに、迷わずに判断するのが大事"
    advide11_description = "迷った時は人に相談した方が解決が早いと思っている為、転職時に少しでも迷った時、早めに他者からの意見を仰ぎ、解決を急ぐことが大事"
    advide12_description = "飽き症、時間にルーズ、遅刻魔な一面すらも許容し、武器である鋭い直観力、ひらめきを評価し、自由に生きられる組織選びが大事"


class TeamMemberDescription(str, Enum):
    team_member1_description = "理想を追い求める完璧主義なアナタに、現実的な見通しを下さり、高い包容力で甘やかしてくれる人"
    team_member2_description = "緊迫した環境が苦手な為、心身落ち着いた雰囲気作りが出来、愛情を注いでくださる面倒見の良い人"
    team_member3_description = "目の前の感情、衝動的な決定をする為、長期視点で捉えて、事前に想定リスクを示唆してくれる人"
    team_member4_description = "束縛が嫌いな為、適度なバランスで、浮遊しがちなアナタを目標を見失わないように、律してくれる人"
    team_member5_description = "プライドが高く、上から頭を押さえつけられることを極めて嫌う為、フラットなコミュニケーションを取れる人"
    team_member6_description = "人間関係は実力、努力を認めた人と狭く深く築くタイプ。ひたむきに努力を続け、良きライバルとなれる人"
    team_member7_description = "他人の意向に従うのが大の苦手で強烈なリーダーシップを持つ為、フォロワータイプで従順な人"
    team_member8_description = "少し奥手で保守的、グズグズしている自分の背中を前向きに押してくれる行動力旺盛な人"
    team_member9_description = "次から次へと湧き上がる創造性豊かなアイデアを具現化してくれる実行、具現化する力がある人"
    team_member10_description = "地道な仕事も嫌がらずスピード感を持って黙々と推進する為、せっかちな部分を許容し誠実で嘘をつかない人"
    team_member11_description = "慎重派で保守的、受け身で打ち解けにくい印象がある為、能動的に声を掛けてくれる優しく包容力のある人"
    team_member12_description = "多少時間にルーズで自由人のアナタを束縛せず、創造性を尊重し伸び伸びと働かせてくださる懐の大きい人"


perosnality_tag_dict: dict[Unsei, Personalitytag] = {
    Unsei.unsei_1: Personalitytag.personality1,
    Unsei.unsei_2: Personalitytag.personality2,
    Unsei.unsei_3: Personalitytag.personality3,
    Unsei.unsei_4: Personalitytag.personality4,
    Unsei.unsei_5: Personalitytag.personality5,
    Unsei.unsei_6: Personalitytag.personality6,
    Unsei.unsei_7: Personalitytag.personality7,
    Unsei.unsei_8: Personalitytag.personality8,
    Unsei.unsei_9: Personalitytag.personality9,
    Unsei.unsei_10: Personalitytag.personality10,
    Unsei.unsei_11: Personalitytag.personality11,
    Unsei.unsei_12: Personalitytag.personality12,
}

personality_dict: dict[Unsei, PersonalityDescription] = {
    Unsei.unsei_1: PersonalityDescription.personality1_description,
    Unsei.unsei_2: PersonalityDescription.personality2_description,
    Unsei.unsei_3: PersonalityDescription.personality3_description,
    Unsei.unsei_4: PersonalityDescription.personality4_description,
    Unsei.unsei_5: PersonalityDescription.personality5_description,
    Unsei.unsei_6: PersonalityDescription.personality6_description,
    Unsei.unsei_7: PersonalityDescription.personality7_description,
    Unsei.unsei_8: PersonalityDescription.personality8_description,
    Unsei.unsei_9: PersonalityDescription.personality9_description,
    Unsei.unsei_10: PersonalityDescription.personality10_description,
    Unsei.unsei_11: PersonalityDescription.personality11_description,
    Unsei.unsei_12: PersonalityDescription.personality12_description,
}

industry_dict: dict[Unsei, list[IndustryTag]] = {
    Unsei.unsei_1: [IndustryTag.industry1, IndustryTag.industry2],
    Unsei.unsei_2: [IndustryTag.industry3, IndustryTag.industry4],
    Unsei.unsei_3: [IndustryTag.industry5, IndustryTag.industry6],
    Unsei.unsei_4: [IndustryTag.industry7, IndustryTag.industry8],
    Unsei.unsei_5: [IndustryTag.industry9, IndustryTag.industry10],
    Unsei.unsei_6: [IndustryTag.industry1, IndustryTag.industry11],
    Unsei.unsei_7: [IndustryTag.industry11, IndustryTag.industry12],
    Unsei.unsei_8: [IndustryTag.industry1, IndustryTag.industry13],
    Unsei.unsei_9: [
        IndustryTag.industry2,
        IndustryTag.industry14,
        IndustryTag.industry15,
    ],
    Unsei.unsei_10: [IndustryTag.industry1, IndustryTag.industry16],
    Unsei.unsei_11: [IndustryTag.industry17, IndustryTag.industry1],
    Unsei.unsei_12: [IndustryTag.industry7, IndustryTag.industry18],
}

industry_personality_description_dict: dict[
    Personalitytag, PersonalityIndustryDescription
] = {
    Personalitytag.personality1: PersonalityIndustryDescription.personality1_description,
    Personalitytag.personality2: PersonalityIndustryDescription.personality2_description,
    Personalitytag.personality3: PersonalityIndustryDescription.personality3_description,
    Personalitytag.personality4: PersonalityIndustryDescription.personality4_description,
    Personalitytag.personality5: PersonalityIndustryDescription.personality5_description,
    Personalitytag.personality6: PersonalityIndustryDescription.personality6_description,
    Personalitytag.personality7: PersonalityIndustryDescription.personality7_description,
    Personalitytag.personality8: PersonalityIndustryDescription.personality8_description,
    Personalitytag.personality9: PersonalityIndustryDescription.personality9_description,
    Personalitytag.personality10: PersonalityIndustryDescription.personality10_description,
    Personalitytag.personality11: PersonalityIndustryDescription.personality11_description,
    Personalitytag.personality12: PersonalityIndustryDescription.personality12_description,
}

industry_field_dict: dict[Unsei, list[IndustryFieldTag]] = {
    Unsei.unsei_1: [
        IndustryFieldTag.industry_field1,
        IndustryFieldTag.industry_field2,
        IndustryFieldTag.industry_field3,
    ],
    Unsei.unsei_2: [IndustryFieldTag.industry_field4, IndustryFieldTag.industry_field5],
    Unsei.unsei_3: [IndustryFieldTag.industry_field6, IndustryFieldTag.industry_field7],
    Unsei.unsei_4: [
        IndustryFieldTag.industry_field8,
        IndustryFieldTag.industry_field9,
        IndustryFieldTag.industry_field10,
    ],
    Unsei.unsei_5: [
        IndustryFieldTag.industry_field11,
        IndustryFieldTag.industry_field12,
    ],
    Unsei.unsei_6: [
        IndustryFieldTag.industry_field1,
        IndustryFieldTag.industry_field13,
    ],
    Unsei.unsei_7: [
        IndustryFieldTag.industry_field14,
    ],
    Unsei.unsei_8: [
        IndustryFieldTag.industry_field1,
        IndustryFieldTag.industry_field15,
        IndustryFieldTag.industry_field16,
    ],
    Unsei.unsei_9: [
        IndustryFieldTag.industry_field9,
        IndustryFieldTag.industry_field17,
        IndustryFieldTag.industry_field18,
    ],
    Unsei.unsei_10: [
        IndustryFieldTag.industry_field19,
        IndustryFieldTag.industry_field4,
    ],
    Unsei.unsei_11: [
        IndustryFieldTag.industry_field20,
        IndustryFieldTag.industry_field1,
    ],
    Unsei.unsei_12: [
        IndustryFieldTag.industry_field21,
        IndustryFieldTag.industry_field14,
    ],
}

industry_field_description_dict: dict[Unsei, IndustryFieldDescription] = {
    Unsei.unsei_1: IndustryFieldDescription.industry_field_description_1,
    Unsei.unsei_2: IndustryFieldDescription.industry_field_description_2,
    Unsei.unsei_3: IndustryFieldDescription.industry_field_description_3,
    Unsei.unsei_4: IndustryFieldDescription.industry_field_description_4,
    Unsei.unsei_5: IndustryFieldDescription.industry_field_description_5,
    Unsei.unsei_6: IndustryFieldDescription.industry_field_description_6,
    Unsei.unsei_7: IndustryFieldDescription.industry_field_description_7,
    Unsei.unsei_8: IndustryFieldDescription.industry_field_description_8,
    Unsei.unsei_9: IndustryFieldDescription.industry_field_description_9,
    Unsei.unsei_10: IndustryFieldDescription.industry_field_description_10,
    Unsei.unsei_11: IndustryFieldDescription.industry_field_description_11,
    Unsei.unsei_12: IndustryFieldDescription.industry_field_description_12,
}

culture_dict: dict[Unsei, list[CultureTag]] = {
    Unsei.unsei_1: [CultureTag.culture1, CultureTag.culture2],
    Unsei.unsei_2: [CultureTag.culture3, CultureTag.culture4],
    Unsei.unsei_3: [CultureTag.culture5, CultureTag.culture6],
    Unsei.unsei_4: [CultureTag.culture7, CultureTag.culture8],
    Unsei.unsei_5: [CultureTag.culture9, CultureTag.culture10],
    Unsei.unsei_6: [CultureTag.culture11, CultureTag.culture12],
    Unsei.unsei_7: [CultureTag.culture1, CultureTag.culture2],
    Unsei.unsei_8: [CultureTag.culture3, CultureTag.culture4],
    Unsei.unsei_9: [CultureTag.culture5, CultureTag.culture6],
    Unsei.unsei_10: [CultureTag.culture7, CultureTag.culture8],
    Unsei.unsei_11: [CultureTag.culture9, CultureTag.culture10],
    Unsei.unsei_12: [CultureTag.culture11, CultureTag.culture12],
}

culture_description_dict: dict[Unsei, CultureTagDescription] = {
    Unsei.unsei_1: CultureTagDescription.culture1_description,
    Unsei.unsei_2: CultureTagDescription.culture2_description,
    Unsei.unsei_3: CultureTagDescription.culture3_description,
    Unsei.unsei_4: CultureTagDescription.culture4_description,
    Unsei.unsei_5: CultureTagDescription.culture5_description,
    Unsei.unsei_6: CultureTagDescription.culture6_description,
    Unsei.unsei_7: CultureTagDescription.culture7_description,
    Unsei.unsei_8: CultureTagDescription.culture8_description,
    Unsei.unsei_9: CultureTagDescription.culture9_description,
    Unsei.unsei_10: CultureTagDescription.culture10_description,
    Unsei.unsei_11: CultureTagDescription.culture11_description,
    Unsei.unsei_12: CultureTagDescription.culture12_description,
}

team_member_dict: dict[Unsei, list[TeamMemberTag]] = {
    Unsei.unsei_1: [TeamMemberTag.team_member1, TeamMemberTag.team_member2],
    Unsei.unsei_2: [TeamMemberTag.team_member3, TeamMemberTag.team_member4],
    Unsei.unsei_3: [TeamMemberTag.team_member5, TeamMemberTag.team_member6],
    Unsei.unsei_4: [TeamMemberTag.team_member7, TeamMemberTag.team_member8],
    Unsei.unsei_5: [TeamMemberTag.team_member9, TeamMemberTag.team_member10],
    Unsei.unsei_6: [TeamMemberTag.team_member11, TeamMemberTag.team_member12],
    Unsei.unsei_7: [TeamMemberTag.team_member1, TeamMemberTag.team_member2],
    Unsei.unsei_8: [TeamMemberTag.team_member3, TeamMemberTag.team_member4],
    Unsei.unsei_9: [TeamMemberTag.team_member5, TeamMemberTag.team_member6],
    Unsei.unsei_10: [TeamMemberTag.team_member7, TeamMemberTag.team_member8],
    Unsei.unsei_11: [TeamMemberTag.team_member9, TeamMemberTag.team_member10],
    Unsei.unsei_12: [TeamMemberTag.team_member11, TeamMemberTag.team_member12],
}

advice_dict: dict[Unsei, list[AdvideTag]] = {
    Unsei.unsei_1: [AdvideTag.advide1, AdvideTag.advide2],
    Unsei.unsei_2: [AdvideTag.advide3, AdvideTag.advide4],
    Unsei.unsei_3: [AdvideTag.advide5, AdvideTag.advide6],
    Unsei.unsei_4: [AdvideTag.advide7, AdvideTag.advide8],
    Unsei.unsei_5: [AdvideTag.advide9, AdvideTag.advide10],
    Unsei.unsei_6: [AdvideTag.advide11, AdvideTag.advide12],
    Unsei.unsei_7: [AdvideTag.advide1, AdvideTag.advide2],
    Unsei.unsei_8: [AdvideTag.advide3, AdvideTag.advide4],
    Unsei.unsei_9: [AdvideTag.advide5, AdvideTag.advide6],
    Unsei.unsei_10: [AdvideTag.advide7, AdvideTag.advide8],
    Unsei.unsei_11: [AdvideTag.advide9, AdvideTag.advide10],
    Unsei.unsei_12: [AdvideTag.advide11, AdvideTag.advide12],
}

advice_description_dict: dict[Unsei, AdvideDescription] = {
    Unsei.unsei_1: AdvideDescription.advide1_description,
    Unsei.unsei_2: AdvideDescription.advide2_description,
    Unsei.unsei_3: AdvideDescription.advide3_description,
    Unsei.unsei_4: AdvideDescription.advide4_description,
    Unsei.unsei_5: AdvideDescription.advide5_description,
    Unsei.unsei_6: AdvideDescription.advide6_description,
    Unsei.unsei_7: AdvideDescription.advide7_description,
    Unsei.unsei_8: AdvideDescription.advide8_description,
    Unsei.unsei_9: AdvideDescription.advide9_description,
    Unsei.unsei_10: AdvideDescription.advide10_description,
    Unsei.unsei_11: AdvideDescription.advide11_description,
    Unsei.unsei_12: AdvideDescription.advide12_description,
}

team_member_description_dict: dict[Unsei, TeamMemberDescription] = {
    Unsei.unsei_1: TeamMemberDescription.team_member1_description,
    Unsei.unsei_2: TeamMemberDescription.team_member2_description,
    Unsei.unsei_3: TeamMemberDescription.team_member3_description,
    Unsei.unsei_4: TeamMemberDescription.team_member4_description,
    Unsei.unsei_5: TeamMemberDescription.team_member5_description,
    Unsei.unsei_6: TeamMemberDescription.team_member6_description,
    Unsei.unsei_7: TeamMemberDescription.team_member7_description,
    Unsei.unsei_8: TeamMemberDescription.team_member8_description,
    Unsei.unsei_9: TeamMemberDescription.team_member9_description,
    Unsei.unsei_10: TeamMemberDescription.team_member10_description,
    Unsei.unsei_11: TeamMemberDescription.team_member11_description,
    Unsei.unsei_12: TeamMemberDescription.team_member12_description,
}


class Unsei12(BaseModel):
    unsei: Unsei
    presonality: Personalitytag
