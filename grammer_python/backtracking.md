# 백트래킹 기반 조합론 알고리즘 정리

## 1. 개요

조합(Combination), 순열(Permutation), 중복조합(Combination with Repetition), 중복순열(Permutation with Repetition)은 모두 **백트래킹(Backtracking)** 알고리즘을 **DFS(깊이 우선 탐색)** 방식으로 수행하는 구조를 공유한다.

- **백트래킹**: 선택 → 재귀 탐색 → 되돌림(undo)을 반복하는 알고리즘 기법
- **DFS**: 한 경로를 끝까지 탐색한 뒤 돌아오는 탐색 전략

트리 형태의 탐색 공간을 DFS로 순회하며, 각 노드에서 선택과 되돌림을 반복하는 것이 공통 골격이다.

## 2. 네 가지 유형의 분류

분류 기준은 두 가지뿐이다: **순서의 유무**와 **중복 허용 여부**.

| 종류 | 순서 | 중복 | 길이 `r` 고정 시 개수 | 예시 (`{A,B,C}`, `r=2`) |
|------|------|------|----------------------|--------------------------|
| 순열 | 있음 | 없음 | `nPr = n!/(n-r)!` | AB, AC, BA, BC, CA, CB |
| 조합 | 없음 | 없음 | `nCr = n!/(r!(n-r)!)` | AB, AC, BC |
| 중복순열 | 있음 | 있음 | `n^r` | AA, AB, AC, BA, BB, BC, CA, CB, CC |
| 중복조합 | 없음 | 있음 | `C(n+r-1, r)` | AA, AB, AC, BB, BC, CC |

정리하면:

- 순서가 의미를 가지면 → **순열 계열**
- 순서가 무의미하면 → **조합 계열**
- 같은 원소의 재사용이 가능하면 → **중복** 접두어 부착

## 3. 유한성 분석

### 전제

- 집합 크기 `n`은 유한
- 집합의 원소는 모두 고유(distinct)
- 길이 `r`은 유한 또는 무한

> **중복 원소가 있는 집합의 경우**: `{A, B, B}`처럼 같은 값이 복수 존재하면, 아래 백트래킹 구현을 그대로 적용할 수 없다. 중복 결과가 발생하기 때문이다. 이 경우 집합을 정렬한 뒤, 같은 깊이에서 동일한 값을 연속으로 선택하지 않도록 가지치기(`if i > start and arr[i] == arr[i-1]: continue`)를 추가해야 한다.

### 길이 `r`이 유한일 때

네 가지 모두 **유한**이다.

| 종류 | 근거 |
|------|------|
| 순열 | 매 단계 선택 수 유한, 깊이 `r`로 제한 |
| 조합 | 가능한 부분집합 수 유한 |
| 중복순열 | `n^r` |
| 중복조합 | `C(n+r-1, r)` |

### 길이 제한이 없을 때

| 종류 | 유한/무한 | 근거 |
|------|----------|------|
| 순열 | 유한 | 재사용 불가 → 최대 길이 `n` |
| 조합 | 유한 | 재사용 불가 → 최대 길이 `n` |
| 중복순열 | 무한 | 같은 원소를 무한히 재사용 가능 |
| 중복조합 | 무한 | 같은 원소를 무한히 재사용 가능 |

핵심 구분:

```
중복 없음 → 최대 길이 n → 유한
중복 있음 → 길이 제한 없으면 무한 확장 → 무한
```

## 4. 탐색 트리 예시 (`S = {A, B, C, D}`, 길이 무제한)

### 4-1. 순열

중복이 불가하므로 깊이가 최대 4에서 종료된다.

```
start
├─ A
│  ├─ AB
│  │  ├─ ABC
│  │  │  └─ ABCD
│  │  └─ ABD
│  │     └─ ABDC
│  ├─ AC
│  │  ├─ ACB
│  │  │  └─ ACBD
│  │  └─ ACD
│  │     └─ ACDB
│  └─ AD
│     ├─ ADB
│     │  └─ ADBC
│     └─ ADC
│        └─ ADCB
├─ B ...
├─ C ...
└─ D ...
```

특징: 선택한 원소를 후보에서 제거하므로 깊이가 증가할수록 선택지가 줄어든다. 전체 결과는 유한하다.

### 4-2. 조합

순서가 무의미하므로 현재 인덱스 이후의 원소만 탐색한다.

```
start
├─ A
│  ├─ AB
│  │  ├─ ABC
│  │  │  └─ ABCD
│  │  └─ ABD
│  ├─ AC
│  │  └─ ACD
│  └─ AD
├─ B
│  ├─ BC
│  │  └─ BCD
│  └─ BD
├─ C
│  └─ CD
└─ D
```

특징: `AB`와 `BA`를 동일하게 취급한다. 순열보다 가지치기가 더 공격적으로 이루어지며, 전체 결과는 유한하다.

### 4-3. 중복순열

매 단계마다 전체 4개 원소를 다시 선택할 수 있다.

```
start
├─ A
│  ├─ AA
│  │  ├─ AAA
│  │  │  ├─ AAAA
│  │  │  │  ├─ AAAAA ...
│  │  │  ├─ AAAB
│  │  │  ├─ AAAC
│  │  │  └─ AAAD
│  │  ├─ AAB
│  │  ├─ AAC
│  │  └─ AAD
│  ├─ AB
│  ├─ AC
│  └─ AD
├─ B ...
├─ C ...
└─ D ...
```

특징: 매 깊이마다 분기 수가 4로 일정하다. 깊이 제한이 없으면 무한히 확장된다. 네 유형 중 가장 빠르게 증가한다.

길이 `r`일 때 개수: `4^r` (r=1: 4, r=2: 16, r=3: 64, r=4: 256)

### 4-4. 중복조합

현재 인덱스 이상만 선택하므로 중복순열보다는 느리게 증가하지만, 여전히 무한이다.

```
start
├─ A
│  ├─ AA
│  │  ├─ AAA
│  │  │  ├─ AAAA
│  │  │  │  ├─ AAAAA ...
│  │  │  ├─ AAAB
│  │  │  ├─ AAAC
│  │  │  └─ AAAD
│  │  ├─ AAB
│  │  ├─ AAC
│  │  └─ AAD
│  ├─ AB
│  │  ├─ ABB
│  │  ├─ ABC
│  │  └─ ABD
│  ├─ AC
│  │  ├─ ACC
│  │  └─ ACD
│  └─ AD
│     └─ ADD
├─ B
│  ├─ BB
│  │  ├─ BBB ...
│  │  ├─ BBC
│  │  └─ BBD
│  ├─ BC
│  └─ BD
├─ C
│  ├─ CC ...
│  └─ CD
└─ D
   ├─ DD ...
```

특징: `AB`는 존재하지만 `BA`는 생성되지 않는다. `AA → AAA → AAAA → ...`는 가능하다. 깊이 제한이 없으면 무한이다.

길이 `r`일 때 개수: `C(r+3, r)` (r=1: 4, r=2: 10, r=3: 20, r=4: 35)

## 5. 공통 백트래킹 틀

네 가지 모두 다음과 같은 일반 구조를 공유한다.

```python
def backtrack(path, candidates, start):
    if 종료조건:
        결과저장(path)
        return

    for i in range(start, len(candidates)):
        x = candidates[i]
        path.append(x)
        backtrack(...)
        path.pop()
```

유형 간 차이를 만드는 변수는 세 가지다:

1. `start`를 다음 재귀에 어떻게 전달하는가
2. `candidates`를 그대로 유지하는가, 현재 원소를 제거하는가
3. 종료조건은 무엇인가

## 6. 유형별 구현

### 6-1. 순열

순서 있음, 중복 없음. 선택한 원소를 후보에서 제거한다.

```python
def permute(arr, r):
    result = []

    def backtrack(path, remaining):
        if len(path) == r:
            result.append(path[:])
            return

        for i in range(len(remaining)):
            path.append(remaining[i])
            backtrack(path, remaining[:i] + remaining[i+1:])
            path.pop()

    backtrack([], arr)
    return result
```

핵심: `remaining`에서 현재 원소를 제거하여 다음 재귀에 전달.

### 6-2. 조합

순서 없음, 중복 없음. 현재 인덱스의 다음(`i+1`)부터 탐색한다.

```python
def combine(arr, r):
    result = []

    def backtrack(start, path):
        if len(path) == r:
            result.append(path[:])
            return

        for i in range(start, len(arr)):
            path.append(arr[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result
```

핵심: 다음 재귀의 시작 인덱스가 `i + 1`. 이전 원소로 되돌아가지 않는다.

### 6-3. 중복순열

순서 있음, 중복 있음. 후보를 제거하지 않고 매번 전체를 사용한다.

```python
def product_like(arr, r):
    result = []

    def backtrack(path):
        if len(path) == r:
            result.append(path[:])
            return

        for i in range(len(arr)):
            path.append(arr[i])
            backtrack(path)
            path.pop()

    backtrack([])
    return result
```

핵심: 매 재귀 호출에서 전체 `arr`을 순회. `start` 인덱스도, 후보 제거도 없다.

### 6-4. 중복조합

순서 없음, 중복 있음. 현재 인덱스(`i`)부터 다시 탐색한다.

```python
def comb_with_replacement(arr, r):
    result = []

    def backtrack(start, path):
        if len(path) == r:
            result.append(path[:])
            return

        for i in range(start, len(arr)):
            path.append(arr[i])
            backtrack(i, path)
            path.pop()

    backtrack(0, [])
    return result
```

핵심: 다음 재귀의 시작 인덱스가 `i + 1`이 아닌 `i`. 같은 원소를 다시 선택할 수 있다.

## 7. 구현 요약

네 유형의 차이는 재귀 호출 시그니처 하나로 압축된다.

| 종류 | 재귀 호출 |
|------|----------|
| 순열 | `backtrack(path, remaining - {현재원소})` |
| 조합 | `backtrack(i + 1, path)` |
| 중복순열 | `backtrack(path)` |
| 중복조합 | `backtrack(i, path)` |

구현상의 판단 기준은 두 가지다:

1. **후보를 제거하는가, 유지하는가** (중복 허용 여부)
2. **다음 시작 인덱스를 어디로 설정하는가** (순서 유무)

### 변수 정의

| 변수 | 타입 | 의미 |
|------|------|------|
| `path` | 배열 | 현재까지 선택한 원소들의 나열 |
| `remaining` | 배열 | 아직 선택하지 않은 후보 원소들 |
| `i` | 정수 | 현재 for 루프의 인덱스. 조합 계열에서 다음 탐색 시작 위치를 결정 |