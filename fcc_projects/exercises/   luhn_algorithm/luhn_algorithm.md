# 🔐 Luhn Algorithm (Card Number Verification)

The **Luhn Algorithm** (also known as the "modulus 10" or "mod 10" algorithm) is a checksum formula used to validate various identification numbers, especially credit card numbers.

---

## 🧠 How It Works:

1. **Reverse the Card Number**:
   - Start from the rightmost digit and work backwards.

2. **Sum of Odd-Position Digits** (right to left):
   - These digits are added directly to a running total.

3. **Even-Position Digits**:
   - Multiply each digit by 2.
   - If the result is greater than or equal to 10, split it and add the individual digits.
     - Example: 8 → 8×2 = 16 → 1 + 6 = 7

4. **Total the Sums**:
   - Add the odd-position sum and the even-position sum.

5. **Validation Check**:
   - If the final total modulo 10 equals 0, the number is **valid**.

---

## ✅ Example:
Card Number: `4111-1111-4555-1142`

After cleaning: `4111111145551142`

Steps:
- Reverse: `2411554551111114`
- Odd digits: `2, 1, 5, 5, 1, 1, 1, 4`
- Even digits: `4, 1, 5, 4, 1, 1, 1, 1`

Final total → if divisible by 10 → VALID

---

## ✅ Benefits of the Luhn Algorithm:

- **Quick Validation**: Detects simple errors like mistyped or transposed digits.
- **Lightweight**: No complex computation or database required.
- **Widely Used**: Credit card numbers, IMEI numbers, and other identifiers use it.

---

## ⚠️ Limitations:

- ❌ **Not Secure**: It’s only a **checksum**, not encryption or fraud prevention.
- ❌ **Easy to Bypass**: Anyone can generate a valid number that passes Luhn, but it doesn't mean the number is linked to an actual account.
- ❌ **No Detection for Swapped Digit Pairs** (e.g., `23` to `32` may still pass).

---

## 🛠️ Use Cases:

- Credit Card Number Validation
- IMEI (Mobile Identifier) Checks
- Government-issued IDs (some countries)

---

## 📌 Final Tip:

The Luhn algorithm is useful **only as a preliminary check**. Actual validation should include contacting the issuing authority (e.g., a payment processor).
