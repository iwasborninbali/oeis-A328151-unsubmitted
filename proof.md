# Proof

Let R(N) count ordered pairs of positive integers (x,y) with x²+y²=N. Let D(N) count those pairs with x<y. Let T(m) count positive integer right triangles of hypotenuse m up to interchange of legs. Then

    R(N) = 2 D(N) + [N=2m² for some integer m>=1].

Indeed every off-diagonal pair occurs in two orders, whereas a diagonal pair exists precisely when N=2m² and is then unique.

For every m>=1, D(m²)=T(m) by definition. Also D(2m²)=T(m): map a triangle with legs u>v>0 to x=u+v>y=u-v>0. Then x²+y²=2m². Conversely, if x>y>0 and x²+y²=2m², x and y have the same parity, so u=(x+y)/2 and v=(x-y)/2 are positive integers with u>v and u²+v²=m². The maps are inverses. Therefore R(2m²)=2T(m)+1.

The odd case follows: R(N) is odd exactly when N=2m², and R(2m²)=2k+1 exactly when T(m)=k. Taking least m gives a(2k+1)=2 A006339(k)².

For k>=1 let B=A093195(k), the least N with D(N)=k. B cannot equal 2m²: otherwise D(m²)=D(2m²)=k with m²<B, contradicting minimality. Thus R(B)=2k. Conversely R(N)=2k forces the diagonal indicator to vanish and D(N)=k, so N>=B. Hence a(2k)=B.

The minima exist for all specified indices. The standard sum-of-two-squares theorem gives r₂(5^(2k))=4(2k+1), counting signed ordered integer pairs. Exactly four are axial; none are diagonal since 5^(2k) is odd. Each remaining orbit of signs and ordering has eight members, so D(5^(2k))=k and T(5^k)=k. Thus all relevant sets are nonempty. For k=0, A006339(0)=1 and a(1)=2; independently a(0)=0. This proof is human-checkable and not formally machine-checked.
