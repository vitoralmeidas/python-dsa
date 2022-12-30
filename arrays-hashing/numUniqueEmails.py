def numUniqueEmails(emails):
    hashSet = set()
    for email in emails:
        local, domain = email.split("@")
        local = local.split("+")[0].replace(".", "")
        hashSet.add(local + '@'+domain)

    return len(hashSet)


print(numUniqueEmails(["test.email+alex@leetcode.com",
      "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]))
