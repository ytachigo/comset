nf = 1 # First residue
nl = 7 # Last residue

traj = ["""parm test.prmtop
trajin main.mdcrd 1 last 10"""]

for i in range(nf, nl + 1):
	filename = 'calpha%d.sh' %i
	f = open(filename, 'w')
	str = """cpptraj <<EOF
%s\n""" % traj[0]

	for j in range(nf, nl + 1):
		if i <= j:
		    str += """distance :%d@CA :%d@CA out calpha%d.dat\n""" %(i, j, i)

	str += """EOF"""
	f.write(str)
	f.close()
