# 문제
`()`, `{}`, `[]`, `<>`, `""`, `''`
이 괄호들을 이용해서 만든 문자열이 제대로 된 문자열인지 확인하고 싶습니다.
* 괄호가 제대로 형성이 안되어있을 때에는 빈 문자열을 돌려주세요.
* 괄호가 제대로 형성이 되어있을 경우에는 현재 문자열에 가장 밑의 괄호에는 얼마나 깊은지를 괄호 사이에 나타내 주세요.
* 답이 여러개일 경우에는 어떤 답을 출력해도 됩니다.

# 제한 사항
문자열의 길이는 10만이하입니다.

## 테스트 셋1
* `(){}[]<>`만 포함되어있습니다.

## 테스트 셋2
* `(){}[]<>`뿐만 아니라 `""''`도 포함되어있습니다.

# 입출력 예시
| 문자열 | 출력 |
|-------|------|
| `()` | `(1)` |
| `[()]` | `[(2)]` |
| `""""` | `"1""1"` 혹은 `""2""` |
| `[(])` | ` ` |
| `'([]({{}})'')'` | `'([3]({{5}})'3')'` |

## 설명
* 세번째 문자열은 `테스트 셋2`에 포함되어 있고, `테스트 셋1`에는 포함되어있지 않습니다.
* 네번째 문자열은 잘못된 문자열입니다.
* 다섯번째 문자열은 첫번째와 두번째의 작은 따움표가 서로 다른 깊이입니다.

# 풀이
* 스택을 하나 두어, 문자열을 스캔하면서 현재 문자가 여는 괄호일 경우 스택에 넣어주고 닫는 괄호의 경우, 스택에서 빼주고 괄호 값을 확인해 준다.
* 다만, 따움표의 경우, 어느게 여는 것이고 어느게 닫는 것인지 확인하려면 쉽지 않아 보였다.
* 스택의 마지막 문자열이 따움표이고, 현재 문자도 같은 따움표일 경우 현재 문자는 닫는 따움표로 처리해 두면 된다.
