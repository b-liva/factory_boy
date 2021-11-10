from factory_boy import AccountFactory, ProfileFactory, FemaleProfileFactory


if __name__ == "__main__":

	accounts = AccountFactory.create_batch(6)
	for account in accounts:
		print(account)
	print("*******************")
	profiles = ProfileFactory.create_batch(6)
	for profile in profiles:
		print(profile)
	print("*******************")
	female_profiles = FemaleProfileFactory.create_batch(8)
	for female_prfile in female_profiles:
		print(female_prfile)
