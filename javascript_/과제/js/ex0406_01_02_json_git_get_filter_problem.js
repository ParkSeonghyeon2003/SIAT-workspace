/** ex0406_01_02_json_git_get_filter_problem.js */

// 엘레멘트 초기화
const btnEl = document.getElementById("btn");
const searchEl = document.getElementById("search");
const statusEl = document.getElementById("status");
const tbodyEl = document.getElementById("tbody");

let jsonArr = null; // JSON Array를 담을 변수

/** 테이블 출력 함수 */
function printTable(dataArr = jsonArr) { // 디폴트는 전체 데이터
  let htmlContent = "";

  dataArr.forEach(user => {
    htmlContent += `<tr>
    <td><strong>${user.id}</strong></td>
    <td>${user.name}</td>
    <td>${user.age}</td>
    <td><span>${user.city}</span></td>
    </tr>`
  });

  tbodyEl.innerHTML = htmlContent;
}

/** 비동기로 JSON 데이터를 로드하는 함수 */
async function loadFullData() {
  // 로딩 중 화면 초기화
  statusEl.textContent = "상태: 데이터 불러오는 중...";
  tbodyEl.innerHTML = "";

  try {
    // 요청
    const requestUrl = "https://raw.githubusercontent.com/hiksyksy1234/json/"
      + "refs/heads/main/users.json";
    const response = await fetch(requestUrl);

    // 응답 체크
    if (!response.ok) throw new Error(`HTTP 오류: ${response.status}`);

    // JSON string to Array
    jsonArr = await response.json();
    if (jsonArr === null) throw new Error("jsonArr가 할당되지 않음");

    // 테이블로 출력
    printTable();
    statusEl.textContent = `상태: 로딩 완료 (총 ${jsonArr.length}명)`;
  } catch (err) { // 에러 처리
    statusEl.textContent = "상태: 오류 발생!";
    tbodyEl.innerHTML = `<tr><td colspan="4">에러: ${err.message}</td></tr>`;
    console.error("데이터 로드 실패:", err);
  }
}

/** 데이터 로드 버튼 클릭 핸들러 */
function btnClick() {
  searchEl.value = "";
  loadFullData();
  searchEl.focus();
}

// 리스너 등록
btnEl.addEventListener("click", btnClick);
searchEl.addEventListener("input", () => {
  if (jsonArr === null) {
    statusEl.textContent = "상태: 먼저 데이터를 불러와 주세요!";
    return;
  }

  const value = searchEl.value.replace(/ /g, ""); // 공백 전부 제거

  // 공백 시 전체 데이터 로드
  if (!value) return loadFullData();
  const filteredArr = jsonArr.filter(({name, age, city}) => {
    return (name.includes(value)
    || age.toString().includes(value)
    || city.toLowerCase().includes(value.toLowerCase()));
  });
  printTable(filteredArr);
  statusEl.textContent = `상태: '${value}' 검색 결과 (${filteredArr.length}건)`;
});

// 초기 실행
loadFullData();