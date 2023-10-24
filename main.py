from src.monad_py import Writer


writer = Writer(10).bind(lambda x: (x*2, f"{x} multiply by 2") ).bind( lambda x : (x // 20, f"{x} divided by 20")).write("End")
result, log = writer.result()
print(result, log)