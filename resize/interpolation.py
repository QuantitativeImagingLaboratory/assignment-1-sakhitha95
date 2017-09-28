class interpolation:

    def linear_interpolation(self, pt1, pt2, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""

        #Write your code for linear interpolation here
        x1=pt1[0]
        y1=pt1[1]
        i1=pt1[2]
        x2=pt2[0]
        y2=pt2[1]
        i2=pt2[2]
        x3=unknown[0]
        y3=unknown[1]
        i3=unknown[2]
        i3=i1*((x2-x3)/(x2-x1)) + i2*((x3-x1)/x2-x3)


        return i3

    def bilinear_interpolation(self, pt1, pt2, pt3, pt4, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        pt1: known point pt3 and f(pt3) or intensity value
        pt2: known point pt4 and f(pt4) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""

        # Write your code for bilinear interpolation here
        # May be you can reuse or call linear interpolatio method to compute this task
        r1 = [unknown[0], pt1[1], 0]
        i1=self.linear_interpolation(pt1,pt2,unknown)
        r1[2]=i1
        r2 = [unknown[0], pt3[1], 0]
        i2 = self.linear_interpolation(pt3, pt4, unknown)
        r2[2] = i2
        fin = self.linear_interpolation(r1, r2, unknown)

        return fin
