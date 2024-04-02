#include <Arduino.h>
#include <Crypto.h>
#include <cmath>

unsigned long modInverse(unsigned long a, unsigned long m) {
  long long m0 = m, t, q;
  long long x0 = 0, x1 = 1;

  if (m == 1) return 0;

  // Apply extended Euclidean algorithm
  while (a > 1) {
    q = a / m;
    t = m;
    m = a % m, a = t;
    t = x0;
    x0 = x1 - q * x0;
    x1 = t;
  }

  if (x1 < 0) x1 += m0;

  return x1;
}

void encrypt(unsigned long plaintext, unsigned long e, unsigned long n, unsigned long &ciphertext) {
  ciphertext = 1;
  for (unsigned long i = 0; i < e; ++i) {
    ciphertext = (ciphertext * plaintext) % n;
  }
}

void decrypt(unsigned long ciphertext, unsigned long d, unsigned long n, unsigned long &decrypted) {
  decrypted = 1;
  for (unsigned long i = 0; i < d; ++i) {
    decrypted = (decrypted * ciphertext) % n;
  }
}

unsigned long p = 61;
unsigned long q = 53;
unsigned long n = p * q;
unsigned long phi_n = (p - 1) * (q - 1);
unsigned long e = 65537;
unsigned long d = modInverse(e, phi_n);

void setup() {
  Serial.begin(9600);

}

void loop() {
  // Nothing to do here
  unsigned long plaintext = 17;
  unsigned long ciphertext;
  encrypt(plaintext, e, n, ciphertext);
  Serial.print("Ciphertext: ");
  Serial.println(ciphertext);

  unsigned long decrypted;
  decrypt(ciphertext, d, n, decrypted);
  Serial.print("Decrypted: ");
  Serial.println(decrypted);
  delay(1000);
}

