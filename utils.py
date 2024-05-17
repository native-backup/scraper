from scraper import Scraper
import asyncio
from bs4 import BeautifulSoup
from typing import cast
from schemas import (
    Unsei,
    perosnality_tag_dict,
    personality_dict,
    industry_dict,
    industry_personality_description_dict,
    industry_field_dict,
    industry_field_description_dict,
    culture_dict,
    culture_description_dict,
    team_member_dict,
    advice_dict,
    advice_description_dict,
    team_member_description_dict,
)


def parse_html(html_string: str) -> str:
    soup = BeautifulSoup(html_string, "html.parser")
    return soup.prettify()


def parse_col(div_tag: str, s: BeautifulSoup) -> list[str]:
    return [
        i.replace(" ", "")
        for i in s.find("div", class_=f"{div_tag}").text.split("\n")
        if i.replace(" ", "") != ""
    ]


def calc_params(
    scraper: Scraper, year: int, month: int, day: int, sex: str
) -> dict[str, int]:
    params = {"行動": 0, "お金": 0, "遊び": 0, "知識": 0, "自立": 0}

    tsuhen = {
        "偏官": "行動",
        "正官": "行動",
        "偏財": "お金",
        "正財": "お金",
        "食神": "遊び",
        "傷官": "遊び",
        "印綬": "知識",
        "偏印": "知識",
        "劫財": "自立",
        "比肩": "自立",
    }

    data = scraper.read_data(year=year, month=month, day=day, sex=sex, limit=10)
    s = BeautifulSoup(parse_html(cast(str, data[0].html_string)), "html.parser")
    div_tsuhen = parse_col("tsuhen", s)
    div_ztsuhen = parse_col("ztsuhen", s)
    params[tsuhen[div_tsuhen[0]]] += 20
    params[tsuhen[div_tsuhen[1]]] += 10
    params[tsuhen[div_tsuhen[0]]] += 30
    params[tsuhen[div_tsuhen[1]]] += 30
    params[tsuhen[div_ztsuhen[0]]] += 10
    unsei12 = parse_col("unsei12", s)
    unsei_enums = [Unsei(i) for i in unsei12]
    personality_tags = [perosnality_tag_dict[i].value for i in unsei_enums]
    return params


html_string = """
<html style="zoom: 140.625%;" xmlns:og="http://ogp.me/ns#">
 <head>
  <title>
   愛され四柱推命
  </title>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1.0, user-scalable=yes" name="viewport"/>
  <script src="./jquery-3.2.1.min.js">
  </script>
  <script>
   (function(){
	    var _UA = navigator.userAgent;
	    if (_UA.indexOf('iPhone') > -1 || _UA.indexOf('iPod') > -1) {
	        document.write('<link href="./top_ios.css?xxx=20170221003" rel="stylesheet" type="text/css" media="all" />');
	    }else if(_UA.indexOf('Android') > -1){
	        document.write('<link href="./top.css?xxx=20170221003" rel="stylesheet" type="text/css" media="all" />');
	    }else{
	        document.write('<link href="./top.css?xxx=20170221003" rel="stylesheet" type="text/css" media="all" />');
	    }
	})();

	// documentが読み込まれたあとの共通処理
	$(document).ready(function(){
		// HTMLの横幅を指定する。
		var HTML_WIDTH = "640";

		$(function() {
		    $(window).resize(function(){ setZoom() });
		    setZoom();
		});

		function setZoom(){
		    var scale = $(window).width() / HTML_WIDTH * 100 + "%";
		    $('html').css({'zoom' : scale });
		}
	});
  </script>
  <link href="./top.css?xxx=20170221003" media="all" rel="stylesheet" type="text/css"/>
 </head>
 <body>
  <div id="wrapper">
   <div id="head_spacer">
   </div>
   <div id="detail_frame_base">
    <div id="detail_frame_top">
     <div class="birth_area_margin">
     </div>
     <div class="birth_area">
      1951年
			1月
			1日
			(0時0分)
			 生 

			女性
     </div>
    </div>
    <div id="detail_frame_body">
     <!--		<div id="detail_frame_left"></div>-->
     <div id="detail_frame_mid">
      <div id="detail_title">
       <div id="detail_title_1">
       </div>
       <div id="detail_title_2">
       </div>
       <div id="detail_title_3">
       </div>
       <div id="detail_title_4">
       </div>
       <div id="detail_title_5">
       </div>
      </div>
      <div id="detail_mid_left">
       <div class="tenchu">
        <div>
         辰巳
        </div>
        <div>
         午未
        </div>
       </div>
       <div class="kanshi">
        <div class="day">
         <div class="k_info_1">
          -金
         </div>
         <div class="k_info_2">
          辛丑
         </div>
         <div class="k_info_3">
          -土
         </div>
        </div>
        <div class="month">
         <div class="k_info_1">
          +土
         </div>
         <div class="k_info_2">
          戊子
         </div>
         <div class="k_info_3">
          +水
         </div>
        </div>
        <div class="year">
         <div class="k_info_1">
          +金
         </div>
         <div class="k_info_2">
          庚寅
         </div>
         <div class="k_info_3">
          +木
         </div>
        </div>
       </div>
       <div class="clearline">
       </div>
       <div id="d_mid_left">
       </div>
       <div id="d_mid_right">
        <div class="kanshi_no">
         <div class="day3">
          38
         </div>
         <div class="month3">
          25
         </div>
         <div class="year3">
          27
         </div>
        </div>
        <div class="zokan">
         <div class="day2">
          己
         </div>
         <div class="month2">
          癸
         </div>
         <div class="year2">
          甲
         </div>
        </div>
        <div class="tsuhen">
         <div class="day2">
         </div>
         <div class="month2">
          印綬
         </div>
         <div class="year2">
          劫財
         </div>
        </div>
        <div class="ztsuhen">
         <div class="day2">
          偏印
         </div>
         <div class="month2">
          食神
         </div>
         <div class="year2">
          正財
         </div>
        </div>
        <div class="unsei12">
         <div class="day2">
          養
         </div>
         <div class="month2">
          長生
         </div>
         <div class="year2">
          胎
         </div>
        </div>
       </div>
       <div class="energy">
        <div class="kei">
         18
        </div>
        <div class="day2">
         6
        </div>
        <div class="month2">
         9
        </div>
        <div class="year2">
         3
        </div>
       </div>
      </div>
      <div id="detail_mid_right">
       <div id="right_title_1">
       </div>
       <div id="right_title_2">
       </div>
       <div id="right_title_3">
       </div>
       <div id="right_title_4">
       </div>
       <div id="right_title_5">
       </div>
       <div id="right_title_6">
       </div>
      </div>
     </div>
     <!--		<div id="detail_frame_right"></div>-->
    </div>
    <div id="detail_frame_foot">
    </div>
   </div>
   <footer>
    <div id="head_logo">
    </div>
    <br/>
    <a href="https://www.aisare-fourpillars.com/" target="_blank">
     愛され四柱推命鑑定師養成スクール公式サイト
    </a>
   </footer>
  </div>
 </body>
</html>

"""
# 0行目
print(parse_col("tenchu", BeautifulSoup(html_string, "html.parser")))
# 一行目
print(parse_col("kanshi", BeautifulSoup(html_string, "html.parser")))
# 二行目
print(parse_col("kanshi_no", BeautifulSoup(html_string, "html.parser")))
# 三行目
print(parse_col("zokan", BeautifulSoup(html_string, "html.parser")))
# 四行目
print(parse_col("tsuhen", BeautifulSoup(html_string, "html.parser")))
# 五行目
print(parse_col("ztsuhen", BeautifulSoup(html_string, "html.parser")))
# 六行目
print(parse_col("unsei12", BeautifulSoup(html_string, "html.parser")))
# 七行目
print(parse_col("energy", BeautifulSoup(html_string, "html.parser")))
