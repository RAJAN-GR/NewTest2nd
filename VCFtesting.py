# This code for testing purpose of ".vcf " file.

import vcf

vcf_reader = vcf.Reader(open(r'D:\Software\Contact manager in smart phones/00001.vcf', 'r'))

for record in vcf_reader:
	print (record,sec)

# that previus changes were not required.
# this edit is from the git hub web.without commit option.
# This 3rd line for checking the commit title and discripastion properly.
