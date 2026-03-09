/* if_input_table.js */
let name = prompt("이름을 입력해주세요.");

let output = "<div class='card'>";
if (name) {
  output += `
    <p>입력한 이름: <span class='bold'>${name}</span></p>
    <table>
      <thead>
        <tr>
          <th>이름</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>${name}</td>
        </tr>
      </tbody>
    </table>
  `;
} else {
  output += "이름이 입력되지 않았습니다.";
}
output += "</div>";

document.body.innerHTML = output;