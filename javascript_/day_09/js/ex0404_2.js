const btn = document.getElementById("btn");
const tbody = document.getElementById("tbody");
const city = document.getElementById("city");

let data = null;

function printTable(jsonData = data) {
  let htmlContent = "";
  jsonData.forEach(user => {
    htmlContent += `<tr>
    <td>${user.id}</td>
    <td>${user.name}</td>
    <td>${user.age}</td>
    <td>${user.city}</td>
    </tr>`;
  });
  tbodyEl.innerHTML = htmlContent;
}

(async () => {
  const status = document.getElementById("status");

  status.classList.remove("success", "error");
  status.textContent = "상태: 데이터 불러오는 중...";
  tbodyEl.innerHTML = "";
  
  try {
    // request
    const response = await fetch("https://raw.githubusercontent.com/hiksyksy1234/json/refs/heads/main/users.json");
    
    // HTTP Error check
    if (!response.ok) {
      throw new Error(`HTTP 오류: ${response.status}`);
    }
    
    // JSON parsing
    data = await response.json();
    // display
    printTable();
    status.classList.add("success");
    status.textContent = "상태: 전체 로딩 성공!";
  } catch (err) {
    status.classList.add("error");
    status.textContent = "상태: 오류 발생!";
    tbodyEl.innerHTML = `<tr><td colspan="4">에러 : ${err.message}</td></tr>`;
    console.error("데이터 로드 실패:", err);
  }
})();

city.addEventListener("change", () => {
  const filteredData = city.value === "all"
    ? data
    : data.filter(user => user.city === city.value);
  printTable(filteredData);
});