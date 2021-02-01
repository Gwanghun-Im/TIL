# boilerplate

```html
<!-- 
  Document Type
  문서 형식(유형)을 정의한다. 

  HTML & CSS 최신버전
-->
<!DOCTYPE html> 

<!-- 
  HTML 문서의 루트를 나타내는 엘리먼트
  lang  속성
  - 웹페이지 안의 모튼 텍스트들에 대한 문서 언어를 지정
 -->
<html lang="zh">
<!-- 
  직접적으로 사용자 눈에 보이지 않는, 
  해당 문서를 나타내는 각종 메타데이터를 정의한다.
  실수로 추가하지 않더라도, 브라우저가 자동으로 추가해준다.
 -->
<head>
  <!-- 
    브라우저가 HTML 페이지를 정확하게 보여주기 위하여,
    페이지에 사용된 문자셋(Character Set)을 정의한다.  
  -->
  <meta charset="UTF-8">
  <!-- 
    웹 페이지가 다양한 디바이스에서 잘 표현될 수 있도록 정의한다. 
    내부적으로 특정한 CSS 코드로 자동으로 해석된다.
   -->
  <meta name="viewport" 
  content="width=device-width, initial-scale=1.0">
  <!-- 
    페이지 제목을 의미하며, 아래 항목에 제공된다.
    - 브라우저 탭 (타이틀 바)
    - 북마크 (즐겨찾기)
    - 검색서비스의 검색결과 목록
   -->
  <title> 보일러플레이트</title>
</head>

<!-- 
  웹 페이지를 방문하는 사용자에게 보여주고 싶은 모든 내용을 정의한다.
 -->
<body>
  <p>
    중국어로 안녕하세요는 
    <span>好</span>라고 합니다.
  </p>
</body>
</html>
```







# HTML 기본문법

## 1. 텍스트와 관련된 주요 태그들

### 1.`<hn>`

> 주로 제목을 표시할 때 많이 사용되며 
>
> 1~6까지 숫자가 들어가 숫자가 커질수록 글씨는 작게 표시됨

### 2.`<p>` ,  `<br>`

> `<p>`태그는 paragraph 의 약자로 문단을 지정하는 태그다.  이 태그는 텍스트를 출력할 경우 한 줄에서 표시할 수 없는 긴 문장은 자동 줄바꿈으로 처리해 준다.
>
> `<br>`태그는 강제로 줄바꿈을 진행 해준다.

### 3.`<strong>` ,  `<b>`

> 두 태그 모두 글씨체를 강조해서 표시할 때 많이 사용하는 태그
>
> 웹페이지로 봐서는 동일한 기능이지만 , `<strong>`에는 의미가 있다

### 4.`<em>` ,  `<i>`

> 어떤 문자를 이탤릭체로 표현할 때 사용 
>
> `<i>`은 sementic적 요소가 존재

### 5.`<span>`

> 특정 부분을 하나의 블록으로 묶어서 강조하거나 스타일 시트를 적용할때 사용
>
> ```html
> <p>오늘만 꿀사과 1박스를 <strong><span style="color:red">1만원</span></strong> 에 판매합니다. </p>
> ```
>
> <p>오늘만 꿀사과 1박스를 <strong><span style="color:red">1만원</span></strong> 에 판매합니다. </p>

## 2. 다양항 목록을 만드는 태그들

### 1.`<ul>` ,  `<li>` 

>주로 순서없는 목록을 만들때 사용
>
>```html
><ul>
>    <li>아침</li>
>    <li>점심</li>
>    <li>저녁</li>
></ul>
>```
>
><ul>
>    <li>아침</li>
>    <li>점심</li>
>    <li>저녁</li>
></ul>

### 2.`<ol> `,  `<li>` 

> 순서가 필요한 목록을 만드는 태그
>
> ```html
> <ol>
>     <li>아침</li>
>     <li>점심</li>
>     <li>저녁</li>
> </ol>
> ```
>
> <ol>
>     <li>아침</li>
>     <li>점심</li>
>     <li>저녁</li>
> </ol>
>
> `<ol type="_">`를 통해 다양한 형태의 순서지정 가능
>
> | 속성 옵션 | 표시값               |
> | --------- | -------------------- |
> | 1         | 숫자(기본값)         |
> | a         | 영문 소문자          |
> | A         | 영문 대문자          |
> | i         | 로마숫자 소문자      |
> | I         | 로마숫자 대문자      |
> | start     | 시작되는 번호 지정   |
> | reversed  | 번호를 역순으로 출력 |
>
> **중첩된 목록 만들기**
>
> ```html
> <ul>
>     <li>외모 가꾸기
>         <ol type="a">
>             <li>양치질</li>
>             <li>머리감기</li>
>         </ol>
>     </li><br>
>     <li>옷 잘입기
>         <ol type="a" start="3">
>             <li>양말신기</li>
>             <li>신결쓰기</li>
>         </ol>
>     </li>
> </ul>
> 
> ```
>
> <ul>
>     <li>외모 가꾸기
>         <ol type="a">
>             <li>양치질</li>
>             <li>머리감기</li>
>         </ol>
>     </li><br>
>     <li>옷 잘입기
>         <ol type="a" start="3">
>             <li>양말신기</li>
>             <li>신결쓰기</li>
>         </ol>
>     </li>
> </ul>

### 3.`<dl>`,  `<dt>`,  `<dd>`  목록 만들기

> `<dl>`태그는 description list 의 약자로 특정 항목과 설명을 한 세트로 묶어서 표시하는 목록을 만들 때 사용한다.
>
> ```html
> <dl>
>     <dt>Korean</dt>
>     	<dd>*name : honggildong</dd>
>     	<dd>*school : best-ing</dd>
>     	<dd>*grade : 3</dd>
>     <dt>English</dt>
>     	<dd>*name : honggildong</dd>
>     	<dd>*school : best-ing</dd>
>     	<dd>*grade : 3</dd>
> </dl>
> ```
>
> <dl>
>     <dt>Korean</dt>
>     	<dd>*name : honggildong</dd>
>     	<dd>*school : best-ing</dd>
>     	<dd>*grade : 3</dd>
>     <dt>English</dt>
>     	<dd>*name : honggildong</dd>
>     	<dd>*school : best-ing</dd>
>     	<dd>*grade : 3</dd>
> </dl>

## 3. 표를 만드는 태그들

### 1. `<table>`, `<tr>`, `<td>` , 기본적인 표 

>표를 만들때 사용하는 기본적인 태그
>
>```html
><h3>표만들기 연습</h3>
><table border="1">
>    <tr>
>        <td>content1</td>
>        <td>content2</td>
>        <td>content3</td>
>    </tr>
>    <tr>
>        <td>content4</td>
>        <td>content5</td>
>        <td>content6</td>
>    </tr>
></table>
>```
>
><h3>표만들기 연습</h3>
><table border="5">
>    <tr>
>        <td>content1</td>
>        <td>content2</td>
>        <td>content3</td>
>    </tr>
>    <tr>
>        <td>content4</td>
>        <td>content5</td>
>        <td>content6</td>
>    </tr>
></table>

### 2. `<thead>`, `<tbody>`, `<tfoot>`

> 표를 제작할때 컬럼 이름, 내용, 요약 부분을 별도로 만들어서 관리하기 위해 사용하는 태그
>
> ```html
> <table border="3">
>     <caption>학생별 식단표</caption>
>     <thead>
>         <tr>
>         	<th>번호</th>
>             <th>학생명</th>
>             <th>좋아하는 메뉴</th>
>         </tr>
>     </thead>
>     <tbody>
>     	<tr>
>         	<td>1</td>
>             <th>홍길동</th>
>             <th>파스타</th>
>         </tr>
>     </tbody>
>     <tfoot>
>     	<tr>
>         	<th>합계</th>
>             <th>1 명</th>
>             <th>8,000원</th></th>
>         </tr>
>     </tfoot>
> </table>
> ```
>
> <table border="3">
>     <caption>학생별 식단표</caption>
>     <thead>
>         <tr>
>         	<th>번호</th>
>             <th>학생명</th>
>             <th>좋아하는 메뉴</th>
>         </tr>
>     </thead>
>     <tbody>
>     	<tr>
>         	<td>1</td>
>             <th>홍길동</th>
>             <th>파스타</th>
>         </tr>
>     </tbody>
>     <tfoot>
>     	<tr>
>         	<th>합계</th>
>             <th>1 명</th>
>             <th>8,000원</th></th>
>         </tr>
>     </tfoot>
> </table>

