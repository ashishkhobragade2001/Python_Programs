def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
    return prefix

strs = ["flower", "flow", "flight"]
print("Longest common prefix:", longest_common_prefix(strs))
# Output: "fl"
