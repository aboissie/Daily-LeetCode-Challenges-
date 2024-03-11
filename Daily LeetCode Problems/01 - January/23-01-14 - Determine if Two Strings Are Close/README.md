# Determine if Two Strings Are Close

## Problem Statement

Given two strings, `word1` and `word2`, determine if they are close. Two strings are considered close if you can attain one from the other using the following operations:

1. **Swap any two existing characters.**
   - For example, transforming `abcde` to `aecdb`.

2. **Transform every occurrence of one existing character into another existing character, and do the same with the other character.**
   - For example, transforming `aacabb` to `bbcaaa` (all 'a's turn into 'b's, and all 'b's turn into 'a's).

You can use the operations on either string as many times as necessary.

The function should return `true` if `word1` and `word2` are close, and `false` otherwise.

