nums = [3,3]
target = 6
if len(nums) > 0:
  for i in range(0, len(nums)):
      for j in range(i+1, len(nums)):
        if i != j:
          sum = nums[i] + nums[j]
          if sum == target:
             print([i,j]) 
      # verificar nums.length != 0
      #   percorrer a lista por linhas
      #     percorrer a lista por colunas
      #       se o index na pos I da linha != index na posicao J coluna
      #         somar numero[i] + numero[j]
      #           verificar se soma == target
      #             retornar os indexes que resultaram a soma