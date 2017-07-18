import tensorflow as tf
import numpy as np

n = 80
initial_value = 1
fib_numbers = np.array( [initial_value, initial_value], dtype=np.int64 )

# Definerer variabler:
fn_minus_2 = tf.Variable(fib_numbers[0], dtype=np.int64)
fn_minus_1 = tf.Variable(fib_numbers[1], dtype=np.int64)
fn = tf.Variable(0, name="N", dtype=np.int64)

# Addisjons funksjonen:
f_add = fn.assign(fn_minus_2 + fn_minus_1)

# Lager funksjon på forhånd for hvordan oppdatere de forskjellige variablene:
update_fn_minus_2 =  fn_minus_2.assign(fn_minus_1)
update_fn_minus_1 =  fn_minus_1.assign(fn)

# initialiserer session og variabler:
session = tf.Session()
session.run(tf.global_variables_initializer())

# Gjør utregningen:
for i in range(n-1):
    fib_numbers = np.append(fib_numbers, session.run(f_add))
    session.run(update_fn_minus_2)
    session.run(update_fn_minus_1)

print(fib_numbers[n])