import decode#importing first game of pathB
Marks=decode.score
if Marks==10:#if score is met then only import the next game else show lost screen
    import threeriddles
    Marks=threeriddles.score
    if Marks>=20:#if score is met then only import the next game else show lost screen
        import guessthenumber
    else:
        import gamelost
        gamelost.lost()
else:
    import gamelost
    gamelost.lost()
