q1 = r"""

MDP of shape <S,A,P,R>:
$$
\begin{aligned}
\mathbf{S} & \subset \ R^{2} \times N\ \times ( N\times N) \ \times \ R\ \times R\times \left( R^{2}\right)^{k}\\
s & =\ ( position,\ energy,\ sampled\ before,value,\ max\ value,\ obstacles) \ \\
\mathbf{A} & =\ \{\ Move\ North,\ Move\ South,\ Move\ East,\ Move\ West,\ Sample\}\\
\mathbf{P}( s'\ |\ s,a) & =\ 1\\
\mathbf{R}( s,a,s') & =\ \begin{cases}
-0.5 & a\ =\ Sample\ \land \ sampled\ before\ \\
1 & a=\ Sample\ \land \ !\ sampled\ before\\
-1 & else
\end{cases}
\end{aligned}
$$

"""


q2 = r"""
 \begin{array}{l}
\begin{aligned}
\mathbf{S} & \subset \ R^{2} \times N\ \times ( N\times N) \ \times \ R\ \times R\times \left( R^{2}\right)^{k}\\
s & =\ ( position,\ energy,\ sampled\ before,value,\ max\ value,\ obstacles) \ \\
\mathbf{A} & =\ \{\ North,\ South,\ East,\ West,\ Sample\}\\
\mathbf{P}( s'\ |\ s,a) & =\ \begin{cases}
0.8 & a\ =move\ action,\ s'\ =\ MoveAction( s) & \\
0.2 & a\ =move\ action,\ s'\ =\ ( WrongTurn( move\ action))( s) & 
\end{cases}\\
\mathbf{R}( s,a,s') & =\ \begin{cases}
-0.5 & a\ =\ Sample\ \land \ sampled\ before\ \\
1 & a=\ Sample\ \land \ !\ sampled\ before\\
-1 & else
\end{cases}
\end{aligned}\\
\\
\ \ WrongTurn( a) \ =\ \begin{cases}
North & a\ =\ East\\
East & a\ =\ South\\
South & a\ =\ West\\
West & a\ =\ North
\end{cases} ,\ MoveAction( s) \ =\ ( s_{x} \ +\ a_{x} ,\ s_{y} +a_{y})\\
\\
( a_{x} ,a_{y}) \ =\ \begin{cases}
( 0,1) & a=North\\
( 1,0) & a=East\\
( 0,-1) & a=South\\
( -1,0) & a=West
\end{cases}
\end{array}
"""


q3 = r"""
_YOUR ANSWER HERE_

_Wrap mathjax syntax with single $ for inline math:_ $x^2 + \frac{y}{2} \cdot \delta = \sum_{i=1}^n \Delta \text{ and } \nabla f$

_Wrap mathjax syntax with double $$ for display math:_
$$x^2 + \frac{y}{2} \cdot \delta = \sum_{i=1}^n\Delta \text{ and } \nabla f$$
"""


q4 = r"""
See `q4a` through `q4e`.
"""


q4a = r"""
_YOUR ANSWER HERE_

_Wrap mathjax syntax with single $ for inline math:_ $x^2 + \frac{y}{2} \cdot \delta = \sum_{i=1}^n \Delta \text{ and } \nabla f$

_Wrap mathjax syntax with double $$ for display math:_
$$x^2 + \frac{y}{2} \cdot \delta = \sum_{i=1}^n\Delta \text{ and } \nabla f$$
"""


q4b = r"""
_YOUR ANSWER HERE_

_Wrap mathjax syntax with single $ for inline math:_ $x^2 + \frac{y}{2} \cdot \delta = \sum_{i=1}^n \Delta \text{ and } \nabla f$

_Wrap mathjax syntax with double $$ for display math:_
$$x^2 + \frac{y}{2} \cdot \delta = \sum_{i=1}^n\Delta \text{ and } \nabla f$$
"""


q4c = r"""
_YOUR ANSWER HERE_

_Wrap mathjax syntax with single $ for inline math:_ $x^2 + \frac{y}{2} \cdot \delta = \sum_{i=1}^n \Delta \text{ and } \nabla f$

_Wrap mathjax syntax with double $$ for display math:_
$$x^2 + \frac{y}{2} \cdot \delta = \sum_{i=1}^n\Delta \text{ and } \nabla f$$
"""


q4d = r"""
_YOUR ANSWER HERE_

_Wrap mathjax syntax with single $ for inline math:_ $x^2 + \frac{y}{2} \cdot \delta = \sum_{i=1}^n \Delta \text{ and } \nabla f$

_Wrap mathjax syntax with double $$ for display math:_
$$x^2 + \frac{y}{2} \cdot \delta = \sum_{i=1}^n\Delta \text{ and } \nabla f$$
"""


q4e = r"""
_YOUR ANSWER HERE_

_Wrap mathjax syntax with single $ for inline math:_ $x^2 + \frac{y}{2} \cdot \delta = \sum_{i=1}^n \Delta \text{ and } \nabla f$

_Wrap mathjax syntax with double $$ for display math:_
$$x^2 + \frac{y}{2} \cdot \delta = \sum_{i=1}^n\Delta \text{ and } \nabla f$$
"""


q5a = r"""
_YOUR ANSWER HERE_

_Wrap mathjax syntax with single $ for inline math:_ $x^2 + \frac{y}{2} \cdot \delta = \sum_{i=1}^n \Delta \text{ and } \nabla f$

_Wrap mathjax syntax with double $$ for display math:_
$$x^2 + \frac{y}{2} \cdot \delta = \sum_{i=1}^n\Delta \text{ and } \nabla f$$
"""


q5b = r"""
_YOUR ANSWER HERE_

_Wrap mathjax syntax with single $ for inline math:_ $x^2 + \frac{y}{2} \cdot \delta = \sum_{i=1}^n \Delta \text{ and } \nabla f$

_Wrap mathjax syntax with double $$ for display math:_
$$x^2 + \frac{y}{2} \cdot \delta = \sum_{i=1}^n\Delta \text{ and } \nabla f$$
"""


q5c = r"""
_YOUR ANSWER HERE_

_Wrap mathjax syntax with single $ for inline math:_ $x^2 + \frac{y}{2} \cdot \delta = \sum_{i=1}^n \Delta \text{ and } \nabla f$

_Wrap mathjax syntax with double $$ for display math:_
$$x^2 + \frac{y}{2} \cdot \delta = \sum_{i=1}^n\Delta \text{ and } \nabla f$$
"""


q5d = r"""
_YOUR ANSWER HERE_

_Wrap mathjax syntax with single $ for inline math:_ $x^2 + \frac{y}{2} \cdot \delta = \sum_{i=1}^n \Delta \text{ and } \nabla f$

_Wrap mathjax syntax with double $$ for display math:_
$$x^2 + \frac{y}{2} \cdot \delta = \sum_{i=1}^n\Delta \text{ and } \nabla f$$
"""


q5e = r"""
_YOUR ANSWER HERE_

_Wrap mathjax syntax with single $ for inline math:_ $x^2 + \frac{y}{2} \cdot \delta = \sum_{i=1}^n \Delta \text{ and } \nabla f$

_Wrap mathjax syntax with double $$ for display math:_
$$x^2 + \frac{y}{2} \cdot \delta = \sum_{i=1}^n\Delta \text{ and } \nabla f$$
"""


q5f = r"""
_YOUR ANSWER HERE_

_Wrap mathjax syntax with single $ for inline math:_ $x^2 + \frac{y}{2} \cdot \delta = \sum_{i=1}^n \Delta \text{ and } \nabla f$

_Wrap mathjax syntax with double $$ for display math:_
$$x^2 + \frac{y}{2} \cdot \delta = \sum_{i=1}^n\Delta \text{ and } \nabla f$$
"""


q5g = r"""
_YOUR ANSWER HERE_

_Wrap mathjax syntax with single $ for inline math:_ $x^2 + \frac{y}{2} \cdot \delta = \sum_{i=1}^n \Delta \text{ and } \nabla f$

_Wrap mathjax syntax with double $$ for display math:_
$$x^2 + \frac{y}{2} \cdot \delta = \sum_{i=1}^n\Delta \text{ and } \nabla f$$
"""


q5h = r"""
_YOUR ANSWER HERE_

_Wrap mathjax syntax with single $ for inline math:_ $x^2 + \frac{y}{2} \cdot \delta = \sum_{i=1}^n \Delta \text{ and } \nabla f$

_Wrap mathjax syntax with double $$ for display math:_
$$x^2 + \frac{y}{2} \cdot \delta = \sum_{i=1}^n\Delta \text{ and } \nabla f$$
"""


q5i = r"""
_YOUR ANSWER HERE_

_Wrap mathjax syntax with single $ for inline math:_ $x^2 + \frac{y}{2} \cdot \delta = \sum_{i=1}^n \Delta \text{ and } \nabla f$

_Wrap mathjax syntax with double $$ for display math:_
$$x^2 + \frac{y}{2} \cdot \delta = \sum_{i=1}^n\Delta \text{ and } \nabla f$$
"""
