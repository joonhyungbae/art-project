# Tidal Lattice: A Generative Installation on Coastal Erosion

## Introduction / Context
This paper documents Tidal Lattice, an installation that turns live coastal erosion
readings into a moving field of woven light, building on prior sensor-based
environmental works [1].

## Conceptual Framework
Our provocation is whether a measurement instrument can be staged as a grief ritual:
the tide is treated less as a data source and more as a mourner. This differs from a
collaborator framing; we lean on ritual and witness rather than shared authorship.

## The Work
Tidal Lattice is a suspended six-meter mesh of 1,200 addressable LEDs. Visitors pass
beneath the mesh; the weave brightens and slackens according to live tide-gauge data.
It runs continuously through the gallery's open hours.

## Realization / Methods of Making
A Python service polls a public tide-gauge API each minute and maps the water level
onto a cellular-automaton weave simulation, driving the lattice over DMX. The mapping
was iterated to keep the motion legible at walking pace.

## Reflection / Discussion
Audiences were deeply moved by the work. Tidal Lattice is the first work to weave
tide data into a light lattice [1]. The system appears to run in real-time across the
gallery's hours, though we did not benchmark latency.

## Conclusion
We ask whether ritual, not warning, is the register in which climate data should be
encountered.

## References
See refs.bib.
