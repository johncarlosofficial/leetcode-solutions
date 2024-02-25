class Solution:

  def simplifyPath(self, path: str):
    directs = []
    temp_direct = ""
    for char in path:
      if char != '/':
        temp_direct += char
      elif char == '/':
        if temp_direct == '..':
          if directs:
            directs.pop()
        elif temp_direct != '.' and temp_direct:
          directs.append(temp_direct)
        temp_direct = ""

    if temp_direct and temp_direct != '.' and temp_direct != '..':
      directs.append(temp_direct)

    ans = "/" + "/".join(directs)

    return ans
