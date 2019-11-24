(defrule is_rectangle 
    (angles ? ? ? ?)
=>
    (assert (shape tetragon))
)

(defrule is_rectangle1
    (sides ? ? ? ?)
=>
    (assert (shape tetragon))
)

(defrule is_triange_acute
    (angles ?x ?y ?z)
    test(< ?x 90)
    test(< ?y 90)
    test(< ?z 90)
=>
    (assert (shape triange_acute))
)

(defrule print-konklus ""(shape ?item)
=>
(printout t "shape :")
(format t "%s%n%n%n" ?item))