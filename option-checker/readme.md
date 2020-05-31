# 개요
오픈 마켓은 판매자가 자유롭게 제품을 팔 수 있도록 등록할 수 있고 구매자가 안전하게 구매할 수 있도록 해주는 플렛폼입니다. 그런데 판매자가 자신의 물건을 많이 노출시키기 위해 터무니없는 가격을 입력하고 있었습니다.

하나의 제품에는 여러가지 옵션을 등록할 수 있으며, 옵션마다 가격을 각각 지정할 수 있습니다. 그리고 옵션 중에서 대표 옵션을 지정해서 구매자의 검색 결과에 노출시킬 수 있습니다. 그런데, 판매자는 사람들이 잘 찾지 않는 하나의 옵션에 터무니없이 낮은 가격을 매겨 구매자를 현혹하고 있었습니다.

이런 현상을 막기 위해 오픈 마켓의 관리자는 고민을 거듭했고, 하나의 정책을 추가했습니다. 그 정책은 다음과 같습니다.
* 대표 옵션 가격의 `lower_bound`%보다 **낮은** 가격을 갖는 옵션이 _없어야 한다._
* 대표 옵션 가격의 `upper_bound`%보다 **높은** 가격을 갖는 옵션이 _없어야 한다._

어떤 상품의 옵션 별 가격 `option_price_list`가 주어졌을 때, 
이 상품에서 대표 옵션으로 지정할 수 있는 옵션이 몇 개 있는지를 
구해서 오픈 마켓의 관리를 편하게 할 수 있도록 도와주세요.

# 제한사항
* `lower_bound`는 0 초과, 100 미만의 정수입니다.
* `upper_bound`는 100 초과, 10,000 미만의 정수입니다.
* `option_price_list`는 0 초과, 10^18 이하의 자연수 리스트입니다.

## 테스트 셋1
* Running Time Limit : 1min
* `option_price_list`의 길이가 1,000 이하입니다.

## 테스트 셋2
* Running Time Limit : 1min
* `option_price_list`의 길이가 100,000 이하이다.

# 입출력 예
| lower_bound | upper_bound | option_price_list | result |
|----------------|----------------|-------------------|--------|
| 80                  | 150                 | [85, 100, 140]     | 1         |

## 입출력 설명
### 첫번째 예시
* 가격이 100인 옵션을 대표 옵션으로 지정하면, 100의 80%인 80보다 낮은 옵션 가격도 없으며, 150%인 150보다 높은 옵션도 없어서 대표 옵션으로 지정할 수 있습니다.
* 가격이 80인 옵션을 대표 옵션으로 하면, 80의 150%인 120보다 높은 140짜리 옵션이 있어서 대표 옵션으로 사용할 수 없습니다. 
* 140의 80%인 112보다 85가 더 작기 때문에 가격이 140인 옵션도 대표 옵션으로 사용할 수 없습니다.
