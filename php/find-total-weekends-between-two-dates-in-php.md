### How to count total weekends between two dates in PHP

```
function compare($startDate, $endDate) {
	$weekends = 0;
	$startDate = new DateTime($startDate);
	$endDate = new DateTime($endDate);

	while($startDate <= $endDate ) {
		$timestamp = strtotime($startDate->format('d-m-Y'));
		$currentDay = strtolower(date('D', $timestamp));
		if (!$weekends && $currentDay == 'sun') {
			$weekends += 1;
		} elseif ($currentDay == 'sat') {
			$weekends += 1;
		}

		$startDate->modify('+1 day');
	}

	return $weekends;
}
```