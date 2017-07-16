#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Title: Primes with runs

import itertools


# https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python
def _try_composite(a, d, n, s):
	if pow(a, d, n) == 1:
		return False
	for i in range(s):
		if pow(a, 2**i * d, n) == n - 1:
			return False
	return True  # n  is definitely composite


def is_prime(n, _precision_for_huge_n=16):
	if n in _known_primes or n in (0, 1):
		return True
	if any((n % p) == 0 for p in _known_primes):
		return False
	d, s = n - 1, 0
	while not d % 2:
		d, s = d >> 1, s + 1
	if n < 1373653:
		return not any(_try_composite(a, d, n, s) for a in (2, 3))
	if n < 25326001:
		return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
	if n < 118670087467:
		if n == 3215031751:
			return False
		return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
	if n < 2152302898747:
		return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
	if n < 3474749660383:
		return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
	if n < 341550071728321:
		return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
	# otherwise
	return not any(_try_composite(a, d, n, s)
		for a in _known_primes[:_precision_for_huge_n])


_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]


# https://stackoverflow.com/a/6285203
def unique_permutations(elements):
	if len(elements) == 1:
		yield (elements[0],)
	else:
		unique_elements = set(elements)
		for first_element in unique_elements:
			remaining_elements = list(elements)
			remaining_elements.remove(first_element)
			for sub_permutation in unique_permutations(remaining_elements):
				yield (first_element,) + sub_permutation


def listToNum(n):
	m = 0
	for i in range(len(n)):
		m += n[-i - 1] * 10 ** i
	return m


length = 10
minimum = 10 ** (length - 1)

pList = []
for i in range(10):
	digit = i
	otherDigits = [x for x in range(10)]
	del(otherDigits[digit])
	primesFound = False
	j = 1
	while not primesFound:
		for p in itertools.combinations_with_replacement(otherDigits, j):
			for n in unique_permutations(p + tuple([digit] * (length - j))):
				m = listToNum(n)
				if m > minimum and is_prime(m):
					pList.append(m)
					primesFound = True
		j += 1

print(sum(pList))
